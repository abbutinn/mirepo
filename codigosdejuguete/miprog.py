
import argparse

print("Funcion con argparse para buscar y crear carpetas")

buscacrea = argparse.ArgumentParser(description='busca y crea carpetas')
buscbuscaacrea.add_argument("-v","--verbose", help="increase output verbosity",
                    action="store_true")
args = buscacrea.parse_args()
if args.verbose:
    print("verbosity turned on")