import msatubemap
from msatubemap.logic.msa2gfa import msa2gfa


def parse_fasta_str(fasta_str):
    fasta_dic = {}
    for tmpline in fasta_str.split('\n'):
        if len(tmpline) < 1:
            continue
        if tmpline[0] == '>':
            if (len(fasta_dic) >= msatubemap.MAX_HAPLOTYPE):  # default: 50
                return fasta_dic
            header = tmpline.rstrip().split()
            seq_name = header[0][1:]
            fasta_dic[seq_name] = ''
        else:
            fasta_dic[seq_name] += tmpline.rstrip()
    return fasta_dic


def parse_fasta_file(fasta_file):
    # TODO: use msatubemap.MAX_HAPLOTYPE
    return msa2gfa.parse_fasta(fasta_file)


def parse_fasta(seq_data):
    if len(seq_data) == 0:
        return {}
    if seq_data[0] == '>':
        return parse_fasta_str(seq_data)
    else:
        return parse_fasta_file(seq_data)


def fa2graph(fasta_dic):
    if len(fasta_dic) == 0:
        return {}
    vg_like_graph, _ = msa2gfa.extract_graph(fasta_dic, 1)
    return vg_like_graph


def get_graph(seq_data):
    fasta_dic = parse_fasta(seq_data)
    return fa2graph(fasta_dic)
