

import pysam
from collections import defaultdict


files=["100000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"100000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"10000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"10000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"20000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"20000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"30000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"30000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"40000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"40000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"50000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"50000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"60000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"60000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"70000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"70000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"80000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"80000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam",
"90000000_130313_cfDNA_2_capt_2_H5W35BCX2_TGTATGCG_connor_dedup.bam",
"90000000_130313_cfDNA_capt_2_H5W35BCX2_TACAGGAT_connor_dedup.bam"]


final={}
file_short_list = []

for file in files:
    file_short = file.split("_S")
    file_short_list.append(file_short[0])
    samfile = pysam.AlignmentFile(file, "rb")
    tags = []

    for line in samfile.fetch():
        t = line.get_tag("X5")
        tags.append(t)

    counts = dict()
    for i in range(10000):
       counts[i] = 0


    for i in tags:
        counts[i] = counts.get(i, 0) + 1

    for x, y in counts.iteritems():
        if x in final:
            final[x].update({file_short[0]: y/2})
        else:
            final.update({x:{file_short[0]: y/2}})

print final
 

with open('temp.txt', 'w') as outf:
    for key, value in final.items():
        outf.write(str(key) + "\t")
        for key2 in value:
            if final[key][key2] >= 1:
                outf.write(str(final[key][key2]) + "\t")
            else:
                outf.write("0" + "\t")
        outf.write("\n")


#for list_item in file_short_list:
#    for key, value in final.items():
#        print final[key][list_item]




 





