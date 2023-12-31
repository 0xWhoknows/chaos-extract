## Chaos Extract

This tool can extract sudomains from `https://chaos.projectdiscovery.io/` and save into output file.

#### Install

```bash
 git clone https://github.com/0xWhoknows/chaos-extract.git && cd chaos-extract
```

#### Usage

```bash
python3 chaosextract.py -h
```

#### Options

- `-c`: Number of concurrent download threads (default 30)
- `-o`: The name and location of the output file
- `-k`: Keywords to filter URLs (e.g., apple google)

#### Example

```bash
python3 chaosextract.py -c 60 -o /tmp/chaos-sub.txt
```