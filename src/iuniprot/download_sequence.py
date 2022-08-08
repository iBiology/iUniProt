#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from io import StringIO
from Bio import SeqIO
import requests

URL = 'https://rest.uniprot.org/uniprotkb'


def download_protein(gene, species='human', fasta='', mode='w'):
    organism_ids = {'human': 9606, 'mouse': 10090}
    if species not in organism_ids:
        print(f'Species {species} not supported yet, only support {", ".join(organism_ids.keys())} for now.')
    oid = organism_ids[species]
    url = f'{URL}/search?query=organism_id:{oid}+AND+gene_exact:{gene}&format=fasta&compressed=false&review=true'
    request = requests.get(url)
    request.raise_for_status()
    records = SeqIO.parse(StringIO(request.text), 'fasta')
    sequence = ''
    for record in records:
        sequence = record.format('fasta')
    if fasta:
        with open(fasta, mode=mode) as o:
            o.write(f'{sequence}\n')
    else:
        print(sequence)
    return sequence


def download_rna(gene):
    pass


if __name__ == '__main__':
    download_protein('Bhlhe40')
