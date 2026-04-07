
from ExifUtil import ExifUtil
from XmpUtil import XmpUtil
from Manager import Manager
from Strings import Strings
from StringAdapter import StringAdapter




def main():
    manager = Manager()

    img_path = r"G:\np\IMAGENS\1_CERRADO (1).JPG"
    folder_path = r"G:\np\img2"

    #field_lookup = _build_field_lookup_table()
    #print(f"Field lookup entries: {len(field_lookup)}\n")

    # Caminho único (arquivo)
    dicionario = manager.collect_metadata(img_path, compute_custom=True)
    print("== Metadados da imagem COM CUSTOM ==")
    print(f"Total campos: {len(dicionario)}")
    print({k: v for k, v in dicionario.items() if 'custom' in k.lower() or k in Strings.CUSTOM_FIELDS})

    # Caminho de pasta
    result_folder = manager.collect_metadata(folder_path, compute_custom=True)
    print("\n== Metadados do diretório COM CUSTOM ==")
    sample = list(result_folder.values())[0]
    print(f"Total campos/foto: {len(sample)}")
    custom_fields = [k for k in sample if k.startswith('time_') or k.startswith('distance_') or k.startswith('voo_id') or k in Strings.CUSTOM_FIELDS]
    print("Exemplo custom fields:", custom_fields[:10])
    print(f"{len(result_folder)} imagens processadas")
    
    # Salvar JSON completo
    import json
    with open('metadata_completa_custom.json', 'w', encoding='utf-8') as f:
        json.dump(result_folder, f, indent=2, ensure_ascii=False, default=str)
    print("\n💾 Salvo: metadata_completa_custom.json")
    with open('tes.json', 'w', encoding='utf-8') as f:
        json.dump(StringAdapter.to_key_label_description(Strings.CUSTOM_FIELDS), f, indent=2, ensure_ascii=False, default=str)
    #print(f"Processamento concluído.{}")


if __name__ == "__main__":
    main()
