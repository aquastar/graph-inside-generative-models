"""Fill results.md from results_template.md and results/tables.md."""
t = open('results/tables.md').read()
parts = {}
for key, chunk in zip(['CLASS', 'CONFUSED', 'GEN', 'BYSTYLE', 'SENS'],
                      __import__('re').split(r'\n(?:CONFUSED|GEN|BYSTYLE|SENS)\n', t)):
    parts[key] = chunk.strip()
s = open('results_template.md').read()
for k, v in parts.items():
    s = s.replace('{' + k + '}', v)
open('results.md', 'w').write(s)
