from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import AlignIO
from Bio import SeqIO, pairwise2
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein, generic_rna, IUPAC
from Bio.SeqUtils import GC
from Bio.Data import CodonTable
from Bio.Blast import NCBIWWW, NCBIXML
import discord
from discord.ext import commands
from discord.utils import get
import os, time, sys
import asyncio
import urllib.request
import matplotlib.pyplot as plt



codex = {"A": "Alanine", "R": "Arginine", "N": "Asparagine", "D": "Aspartate", "C": "Cysteine", "E": "Glutamate",
         "Q": "Glutamine", "G": "Glycine", "H": "Histidine", "I": "Isoleucine", "L": "Leucine", "K": "Lysine",
         "M": "Methionine", "F": "Phenylalanine", "P": "Proline", "S": "Serine", "T": "Threonine",
         "W": "Tryptophan", "Y": "Tyrosine", "V": "Valine", "*": "Stop Codon"}

client = commands.Bot(command_prefix = "$")
class BioP(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        # functions in a class need this to function
        print("Ready to Transcribe Boss")
   
    @commands.command(aliases = ["transcribe"], help = "Transcribes a Coding DNA transcript")
    async def Transcribe(self, ctx, arg1):
        seq1 = Seq(str(arg1), generic_dna)
        transcript =  seq1.transcribe()
        await ctx.send("your coding DNA strand, transcribed is: " + str(transcript))
    
    @commands.command(aliases = ["translate"], help = "Translates a mammalian DNA strans (make sure it's mammalian)")
    async def Translate(self, ctx, arg1):
        global codex
        await ctx.send("Make sure you're giving the 5' --> 3' coding dna strand into this function, not the 3' --> 5' template strand")
        coding_dna = Seq(str(arg1), generic_dna)
        x = coding_dna.translate(to_stop = True) # end ealry if you hit a stop codon
        await ctx.send("Your translated protein has a transcript of: " + str(x))
        print(x)
        
        if len(str(x)) + 1 < len(arg1) / 3:
             await ctx.send("Translation was cut short by a stop codon. The protein lost " + str(len(arg1) / 3 - len(str(x)) - 1) + " amino acids.")
        
        for i in range(0,len(str(x))):
            if str(x)[i] in codex:
                
                await ctx.send("Residue " + str(i + 1) + " is the amino acid " + str(codex[str(x)[i]]))
                
    @commands.command(aliases= ["GC%", "gc", "gc%"], help = "Finds thepercentage of G + C in your DNA strand")
    
    async def GC(self, ctx, arg1):
        
        x = Seq(str(arg1), IUPAC.unambiguous_dna)
        await ctx.send("The percentage of G's and C's in this transcript is: " + str(GC(x.upper())) + "%")
        
        
    @commands.command(aliases = ["ReverseCompliment", "reverse"], help = "Finds the Reverse Compliment of a DNA strand")
    async def Reverse(self, ctx, arg1):
        x = Seq(arg1, IUPAC.unambiguous_dna)
        await ctx.send("The reverse compliment of your transcript is: " + str(x.reverse_complement()))
    
    @commands.command(aliases = ["Compliment", "Comp"], help = "Finds the Complimentary strand of a DNA strand")
    async def comp(self, ctx, arg1):
        x = Seq(arg1, IUPAC.unambiguous_dna)
        await ctx.send("The compliment of your transcript is: " + str(x.complement()))
    
    @commands.command(aliases = ["TranslateBacterial", "TransBacterial"], help = "Translates coding DNA of Bacteria specifically, make sure you have bacterial DNA" )
    async def translatebacterial(self, ctx, arg1):
        coding_dna = Seq(str(arg1), generic_dna)
        x = coding_dna.translate(table = "Bacterial")
        await ctx.send("Your translated protein has a transcript of: " + str(x))
  
        
        if len(str(x)) + 1 < len(arg1) / 3:
             await ctx.send("Translation was cut short by a stop codon. The protein lost " + str(len(arg1) / 3 - len(str(x)) - 1) + " amino acids.")
        
        for i in range(0,len(str(x))):
            if str(x)[i] in codex:
                
                await ctx.send("Residue " + str(i + 1) + " is the amino acid " + str(codex[str(x)[i]]))
                
    
    @commands.command(aliases = ["RNAcodontable"], help = "Print's out the standard codon table")
    async def RNACodonTable(self, ctx):
        table = CodonTable.unambiguous_rna_by_name["Standard"]
        await ctx.send(table)
    
    @commands.command(aliases = ["DNAcodontable"], help = "Print's out the standard codon table")
    async def DNACodonTable(self, ctx):
        table = CodonTable.unambiguous_dna_by_name["Standard"]
        await ctx.send(table)
    
    @commands.command(aliases = ["CompareDNA"], help = "Determines the alignment of a DNA transcript with x number of other transcripts")
    async def Comparedna(self, ctx, *args):
        
        test = []
        bagels = 1
        
        
        for i in range(0, len(args)):
            test.append(Seq(str(args[i])))
            
        
        for i in range(1, len(test)):
            
            if test[0] == test[i]:
                
                await ctx.send(str(test[0]) + " and " + str(test[i]) + " have 100% alignment")
            
            else:
                
                counter = 0
               
                for i in range(0,len(test[0])):
                    if test[0][i] == test[bagels][i]:
                        counter += 1
                      
               
                
                await ctx.send("The alignment between the original transcript and transcript " + str(bagels + 1) + " is " + str(counter / (len(test[0])) * 100) + "%")
            
            bagels += 1
    
    @commands.command(aliases = ["PhylogeneticTree", "Phylogeny"], help = "Makes a Phylogenetic Tree given user inputs")
    async def Phylo(self, ctx, *args):
        
        test = []
        namelist = []
        DNAlist = []
        empty = ""
        
        print(len(args))
        if len(args) == 0:
            pass
        
        else:
            
            for i in range(0, len(args)):
                test.append(str(args[i]))
        
            for i in range(0, len(test)):
            
                if "!" in test[i]:
                    namelist.append(test[i][0:len(test[i]) - 1])
                else:
                    empty += str(test[i])
                    
        DNAlist.append(Seq(empty))
        print(DNAlist)
        
        
        
        fh = open("Wuschel.fasta", "a+")
        print(len(namelist))
        if len(namelist) == 0:
            pass
        
        else:
            
            for i in range(0, len(namelist)):
                print(i)
                if namelist[i] not in "Wuschel.fasta" and str(DNAlist[i]) not in "Wuschel.fasta":
                    fh.write("\n" + ">" + namelist[i] + " ")
                    fh.write(str(DNAlist[i]))
            fh.close()
            await ctx.send("I think it went in the text file?")
        
        
       
        align = AlignIO.read("Wuschel.fasta", "fasta")
        print(align)
        # Calculating distance matrix
        calculator = DistanceCalculator("identity")
        dm  = calculator.get_distance(align)
        
        constructor = DistanceTreeConstructor()
        trees = constructor.upgma(dm)

        # Draw the Tree
        
        Phylo.draw(trees, do_show = False)

        plt.savefig(fname = "PhyloTree")
        with open("PhyloTree.png","rb") as tacos:
            t = discord.File(tacos, filename = "PhyloTree.png")
        await ctx.send(file = t)
        os.remove('PhyloTree.png')
        
    @commands.command(aliases = ["CodonOpt", "Optimize"], help = "Optimizes a DNA sequence, given DNA, the unoptimized codon and the optimized codon")
    async def CodonOptimization(self, ctx, *args):
        try:
            counter = 1
            x = ""
            answer = []
            temp = []
            temp2 = []
           
            temp2.append(args[0].lower())
            
            for i in range(len(temp2[0])):
                if counter % 3 == 0:
                    temp.append(temp2[0][counter - 3])
                    temp.append(temp2[0][counter - 2])
                    temp.append(temp2[0][counter-1])
                    x += temp[0] + temp[1] + temp[2]
                    answer.append(x)
                    x = ""
                    temp.clear()
                    
                    counter += 1
                else:
                    counter += 1
                    
            print(answer)
            print(len(answer) * 3)
            
            for i in range(len(answer)):
                if answer[i].lower() == args[1].lower():
                    answer[i] = args[2].lower()
                    x += answer[i]
                else:
                    x += answer[i]
            print(x)
            
            #await ctx.send("The sequence " + temp2[0] + "\n" + "\n" +  "Optimized is now: " + str(x).upper())
            await ctx.send("The sequence " + temp2[0].upper() + "\n" + "\n"+ "Optimized is now: " + "\n" + "\n")
            await ctx.send(str(x).upper())
                           #+ "\n" + "\n" +  "Optimized is now: " + str(x).upper())
            
                
        
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")
            await ctx.send(str(sys.exc_info()[0]))
            await ctx.send(str(sys.exc_info()[1]))
           
    @commands.command(aliases = ["Tree"], help = "Constructs a Phylogenetic Tree based on a given Fasta File")
    async def PTree(self, ctx):
        
        await ctx.send("Use $PTree_Help if you're not sure how to use this command in conjuction with $Download")
        align = AlignIO.read("Seqs.phy", "phylip")
        
        # Calculating distance matrix
        calculator = DistanceCalculator("identity")
      
        
        dm  = calculator.get_distance(align)
        
        constructor = DistanceTreeConstructor()

        trees = constructor.upgma(dm)
    
        # Draw the Tree
        
        Phylo.draw(trees, do_show = False)
        
        plt.savefig(fname = "PhyloTree")
        with open("PhyloTree.png","rb") as tacos:
            t = discord.File(tacos, filename = "PhyloTree.png")
        await ctx.send(file = t)
        os.remove('PhyloTree.png')
    
    @commands.command(aliases = ["PTree_Help", "Tree_Help"], help = ("Explains the steps to using PTree"))
    async def Phylo_Help(self, ctx):
        
        await ctx.send("""There are certain steps you need to take in order to make a Phylogenetic Tree
currently on the end-user side. First, go on blast and collect protein
alignments for the Tree. BLast automatically selects all, so unselect All
and keep 10 or so alignments. Second, Click Multiple Alignment report
above the selected sequences, it should look like this screenshot: """)
        
        await ctx.send("." + "\n")
        time.sleep(5)
        
        with open("Screen.png","rb") as tacos:
            t = discord.File(tacos, filename = "Screen.png")
        await ctx.send(file = t)
        
        await ctx.send("." + "\n")
        time.sleep(5)
        
        await ctx.send("""Once you have your alignments, you may have to select your desired sequences once
again. At the top of the screen, you should see 'Download' together with a
dropdrown menu. You want to download the 'Fasta plus Gaps' format.""")

        await ctx.send("." + "\n")
        time.sleep(5)
        
        with open("Shot.png","rb") as tacos:
            t = discord.File(tacos, filename = "Shot.png")
        await ctx.send(file = t)
        
        await ctx.send("." + "\n")
        time.sleep(5)
        
        await ctx.send("""The hard part's finally over, thank me. Once you have the file, execute my Download
command with $Download. You'll be prompted to insert an attachment, which you
can do so with the plus icon next to the text box. Select the file you just
downloaded, and press Okay or whatever system prompt to send it in. Lastly,
you just have to execute $PTree, and your phylogenetic tree will be displayed in the chat.""")
                       
        
                       
                      
        
                           
    @commands.command(aliases = ["PairwiseAlignment", "PairAlignment"], help = ("Makes a Pairwise alignment of 2 protein sequences"))
    async def PairAlign(self, ctx, *args):
        try:
            print(len(args))
            x = ""
            counter = 0
            temp = []
            for i in range(len(args)):
                if "!" in args[i]:
                    counter += 1
                if counter == 2:
                    temp.append(x)
                    x = ""
                    counter += 1
                else:
                    if "!" in args[i]:
                        x += str(args[i][1:])
                    else:
                        x += str(args[i])
                    
            if x not in temp:
            
                temp.append(x)
        
            alignments = pairwise2.align.globalxx(Seq(temp[0]), Seq(temp[1]))
        
            result = pairwise2.format_alignment(*alignments[0])
            await ctx.send("Your sequences have an alignment score of: " + "\n" + result[len(result)-10:])
        
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")

            await ctx.send(str(sys.exc_info()[0]))
            await ctx.send(str(sys.exc_info()[1]))
            
    
    @commands.command(aliases = ["blast"], help = ("Blasts a certain query based on input. This version works based on nucleotides only, so supply only your DNA sequence. For example, $Blast AACTTGTACCATGTA"))
    async def Blast(self, ctx, *args):
        await ctx.send("Just be aware that this will take a while. It IS blast after all...")
        
        temp = []
        for i in range(len(args)):
            temp.append(str(args[i]))
        
        if len(temp) != 1:
            await ctx.send("Fatal Error! Something went wrong when I appended your DNA string, contact the Head Pastiere if you can't solve the issue.")
        try:
            
            x = NCBIWWW.qblast("blastn", "nt", Seq(temp[0], generic_dna))
            records = NCBIXML.parse(x)
            for record in records:
                for alignment in record.alignments:
                    for e in alignment.hsps:
                        await ctx.send("****Alignment****")
                        await ctx.send("Sequence:", alignment.title)
                        await ctx.send("Length:", alignment.length)
                        await ctx.send("e value:", e.expect)
                        await ctx.send(e.query[0:50] + "...")
                        await ctx.send(e.match[0:50] + "...")
                        await ctx.send(e.sbjct[0:50] + "...")
                       
        except:
            await ctx.send("An error occured, please check your input or contact the Head Pastiere")
            
            
    
    
    
  
                      
                 
def setup(client):
    
    client.add_cog(BioP(client))
