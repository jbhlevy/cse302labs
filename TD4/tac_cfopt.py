"""
Compiler pass that performs the control flow optimization using CFG representation.
"""

import sys
import argparse
import json
from bx2tac import Instruction, Prog
import AST
import getopt

class Basicblock:
    def __init__(self, instrs):
        self.label = instrs[0].args[0]
        self.instrs = instrs
        self.child = []
        self.parent = []

    def add_parent(self, p_label):
        self.parent.append(p_label)

    def add_child(self, c_label):
        self.child.append(c_label)

    def __str__(self):
        return f'Label: {self.label} ; Instructions: {self.instrs}'

    def merge(self, block):
        self.instrs += block.instrs
        for child_label in block.child:
            self.child.append(child_label)

class CFG:
    def __init__(self, tac_file, proc_name):
        self.name = proc_name[1:]
        self.block_inference(tac_file)
        

    # construct the basic blocks from the instructions
    def block_inference(self, tac_file):
        self.block = dict()

        cond_jumps = {'je', 'jnz', 'jl', 'jle', 'jnl', 'jnle', 'jge', 'jg', 'jz'}

        # Add an entry label before first instruction if needed
        #print(f"\nLocation: block_inference function, tac_file = {tac_file}")
        if (tac_file[0].opcode != 'label'):
            lentry = ".Lentry_" + self.name
            tac_file.insert(0, Instruction('label', [lentry], None))
            self.entry_label = lentry
            #print("SELF.ENTRY_LABEL1 BELOW")
            #print(self.entry_label)
        else:
            self.entry_label = tac_file[0].args[0]
            #print("SELF.ENTRY_LABEL2 BELOW")
            #print(self.entry_label)

        count_label = 0
        tac_add = []

        for i in range(len(tac_file)):
            #print(tac_file[i])

            # For jumps, add a label after the instruction if one doesn’t already exist
            if (tac_file[i].opcode == 'jmp') and (i < (len(tac_file) - 1)) and (tac_file[i + 1].opcode != 'label'):
                new = Instruction('label', [f'.Ljmp_{self.name}_{count_label}'], None)
                count_label += 1
                tac_add.append((i + 1, new))
                #print("a")
                #print(new)

            #Add explicit jmps for fall-throughs.
            if (i >= 1) and (tac_file[i].opcode == 'label') and (tac_file[i - 1].opcode != 'jmp'):
                #print("b:", tac_file[i])
                new = Instruction('jmp', [tac_file[i].args[0]], None)
                tac_add.append((i, new))

            #keep this or not?
            if (i == len(tac_file)-1) and (tac_file[i].opcode != 'jmp') and (tac_file[i].opcode != 'ret'):
                new = Instruction('ret', [], None)
                tac_add.append((i+1, new))

        for i in range(len(tac_add)):
            (index, instr) = tac_add[i]
            tac_file.insert(index+i, instr)

        edges = []
        b_instr = []

        # Start a new block at each label
        #print("start new block at each label in", tac_file)

        for i in range(len(tac_file)):
            #print(tac_file[i])
            #accumulate instructions in the block until...
            b_instr.append(tac_file[i])
            #...encountering a jump
            if tac_file[i].opcode == 'jmp':
                # block until jmp instruction built
                #print("printing block a")
                new = Basicblock(b_instr)
                self.block[new.label] = new
                dest_label = tac_file[i].args[0]
                #print("printing labels")
                #print((new.label, dest_label))
                edges.append((new.label, dest_label))
                #print(edges)
                b_instr = []
            #...a ret
            elif tac_file[i].opcode == 'ret':
                #print("printing block b")
                new = Basicblock(b_instr)
                self.block[new.label] = new
                b_instr = []
            #...or another label (cond jmps)
            elif tac_file[i].opcode in cond_jumps:
                #print("printing block c")
                source = b_instr[0].args[0]
                dest_label = tac_file[i].args[1]
                #print("printing labels")
                #print((source, dest_label))
                edges.append((source, dest_label))
                #print(edges)   
                   
        #print("edges before children added")
        #print(edges) 
        for (parent, child) in edges:
            #print('before')
            #print(self.block[parent])
            self.block[parent].add_child(child)
            #print('printing keys')
            #print(self.block.keys())
            self.block[child].add_parent(parent)
        #print("edges after children added")
        #print(edges)
        

        #print("block inference done")


    def serialize(self, f=True):
        """
        Turns CFG back into an ordinary TAC sequence
        """
        #print(self.block)
        #print(self.block[self.entry_label])
        entry_b = self.block[self.entry_label]
       # print('ENTRY_B BELOW')
        #print(entry_b)
        serialized_instrs = list(entry_b.instrs)
        serialized_labels = set([self.entry_label])

        def UCE(block):
            """
            Unreachable Code Elimination
            - runs after every simplification, particularly jump threading
            - all unreachable blocks are safely removed from the CFG
            """
            for child_label in block.child:
                if child_label not in serialized_labels:
                    # Add current block to schedule
                    serialized_instrs.extend(self.block[child_label].instrs)
                    serialized_labels.add(child_label)
                    UCE(self.block[child_label])
                    #print("HERE")

        # Start with the block with the entry label
        UCE(entry_b)

        if f:
            jmps_to_simplify = []   ## Fall-Through
            for i in range(len(serialized_instrs) - 1):
                current_instr = serialized_instrs[i]
                if current_instr.opcode == 'jmp':
                    next_instr = serialized_instrs[i + 1]
                    if next_instr.opcode == 'label' and next_instr.args[0] == current_instr.args[0]:
                        jmps_to_simplify.append(i)

            if len(jmps_to_simplify) > 0:
                #put them in right order before deleting
                jmps_to_simplify.reverse()
                for i in jmps_to_simplify:
                    serialized_instrs.pop(i)

        return serialized_instrs

    def perform_UCE(self):
        serialized = self.serialize(False)
        #for i in serialized:
        #    print(str(i))
        self.block_inference(serialized)

    def jump_thread(self):

        def linear_seq_of_blocks(block, current_lin_seq):
            if len(block.child) == 1:
                child_label = list(block.child)[0]
                block = self.block[child_label]
                if (len(block.parent) == 1):
                    current_lin_seq += [child_label]
                    return linear_seq_of_blocks(block, current_lin_seq)
            return current_lin_seq

        old_labels = set()

        for label, block in self.block.items():

            # Jump Threading: Sequencing Unconditional Jumps

            cond_jumps = {'je', 'jnz', 'jl', 'jle', 'jnl', 'jnle'}

            lin_seq_of_block_labels = linear_seq_of_blocks(block, [label])[:-1]

            if len(lin_seq_of_block_labels) > 1:
                modified = True

                for i in range(len(lin_seq_of_block_labels) - 1):
                    # Only continue if each of B_2,...,B_{n-2} have empty bodies
                    blockseq = self.block[lin_seq_of_block_labels[i]].instrs[1:-1]
                    if len(blockseq) != 0:
                        modified = False
                        break

                # Change the jmp instruction in B1 to point to Bn instead, so that next(B1) = {Bn}
                if modified:
                    init_block = self.block[lin_seq_of_block_labels[0]]
                    init_block.instrs[-1].args[0] = lin_seq_of_block_labels[-1]
                    # Merge blocks into first_block
                    for i in lin_seq_of_block_labels[1:-1]:
                        init_block.merge(self.block[i])
                        old_labels.add(i)

            # Jump Threading: Turning Conditional into Unconditional Jumps

            for child_label in block.child:
                cond_temp = None
                # If there is a conditional jump from block to the child block
                for i in block.instrs:
                    if (i.opcode in cond_jumps) and (i.args[1] == child_label):
                        cond_temp = i.args[0]
                        cond_jump = i.opcode

                if not cond_temp:
                    continue

                # Verify that cond_temp isn't modified in the child block
                modified = False
                c_block = self.block[child_label]
                for i in c_block.instrs:
                    if i.result == cond_temp:
                        modified = True
                        break
                if modified:
                    continue

                # Verify that a same cond_jump with the same cond_temp is in child block
                for i in range(len(c_block.instrs) - 1):
                    if (c_block.instrs[i].opcode == cond_jump) and (c_block.instrs[i].args[0] == cond_temp):
                        nextlabel = c_block.instrs[i].args[1]
                        c_block.instrs[i].opcode = 'nop'
                        if c_block.instrs[i + 1].opcode == 'jmp':
                            c_block.instrs[i + 1].args[0] = nextlabel

        # Delete blocks after merge
        for i in old_labels:
            self.block.pop(i, None)

    def coalesce(self):
        """
        Coalescing of linear chains of blocks
        Done after every other CFG simplification phase
        """
        old_label = None
        for block in list(self.block.values()):
            # only 1 child
            if len(block.child) == 1:
                child_label = list(block.child)[0]
                child_block = self.block[child_label]
                # if the child block has only 1 parent and if it's not the entry block
                if (len(child_block.parent) == 1) and (child_label != self.entry_label):
                    # if the end of the parent block is 'jmp'
                    if block.instrs[-1].opcode == 'jmp':
                        # delete that last jmp
                        block.instrs[-1].opcode = 'nop'
                        # Merge both blocks
                        block.merge(child_block)
                        # child label will be deleted
                        old_label = child_label
                        break
        
        if old_label:
            self.block.pop(old_label)
            for block in self.block.values():
                # delete old labels from the child blocks
                if old_label in block.child:
                    block.child.remove(old_label)
                # delete old labels from the parent blocks
                if old_label in block.parent:
                    block.parent.remove(old_label)
            return (block.label, old_label)
        else:
            return False

    def coalescing(self):
        coalesced = set()
        while True:
            now_coalescing = self.coalesce()
            self.perform_UCE()
            #dead code cleaned
            if now_coalescing and (now_coalescing not in coalesced):
                coalesced.add(now_coalescing)
            else:
                break

    def control_flow_optimization(self):
        """
        1. Jump threading (conditional & unconditional)
        2. UCE
        3. Coalescing
        """
        self.jump_thread()
        self.perform_UCE()
        self.coalescing()
        #print("FINISHED CF optimization")


#-------------------------------------------------------------------------------
#COMPLETE LOADING FILE

import bx2tac


def optimization(filename):
    gvars = []
    procs = []
    with open(filename, 'r') as fp:
        js_obj = json.load(fp)

    for decl in js_obj:
        #print(decl)
        if "proc" in decl:
            tac = []
            for line in decl["body"]: 
                #print("LINE:", line, "\n")
                arg1 = None
                arg2 = None
                if (len(line["args"]) == 1):
                    arg1 = line["args"][0]
                    #print(arg1)
                elif (len(line["args"]) == 2):
                    arg1 = line["args"][0]
                    arg2 = line["args"][1]
                    #print(arg1)
                    #print(arg2)
                tac.append(bx2tac.Instruction(line["opcode"], [arg1, arg2], line["result"]))

            #print(f"CFG PRINTING, tac = {tac}")
            if tac != []:
                cfg = CFG(tac, decl["proc"])
                #print(cfg, "!!!!!!!!!!!!!!!!!!!!!!!!")
                cfg.control_flow_optimization()
                proc_instrs = cfg.serialize()
                body = []
                for instr in proc_instrs:
                    body.append(instr.js_obj)
                procs.append({"proc": decl["proc"], "args": decl["args"], "body": body})
            else:
                pass
                #If procedure body is empty
                arg1, arg2 = None, None
                body = []
                procs.append({"proc": decl["proc"], "args": decl["args"], "body": body})


        elif "var" in decl:
            #result.append(AST.VarDecl(None, decl["var"], decl["init"], None))
            gvars.append(decl)

    # Write to file
    #print("Optimization done - Writing file")
    all = gvars+procs
    with open(f'{filename[:-9]}.optimized_tac.json', 'w') as tac_file:
        json.dump(all, tac_file)

    # for decl in all:
    #     print(decl)

    #print(f'[[ Output {filename[:-9]}.optimized_tac.json ]]')
    tac_name = f'{filename[:-9]}.optimized_tac.json'
    return tac_name


if __name__ == "__main__":
    opts, file = getopt.getopt(sys.argv[1:], '', [])
    optimization(file[0])
