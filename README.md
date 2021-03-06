# MSA Tube Map

MSA Tube Map is a wrapper of [Sequence Tube Maps](https://github.com/vgteam/sequenceTubeMap)

## Usage

### Online Version

Go to `https://msatubemap.herokuapp.com/msatubemap`

### Run on your local environment

#### Dependencies

* [pipenv](https://github.com/pypa/pipenv)

#### Run

```bash
git clone --recursive https://github.com/hanzou666/msa_tubemap.git
cd msa_tubemap
pipenv install
pipenv run start
```

Go to `http://localhost:5042/msatubemap`

### Input file

MSA Tube Map uses a FASTA format file after multiple sequence alignment.
Either nucleotide or protein sequences are acceptable.
