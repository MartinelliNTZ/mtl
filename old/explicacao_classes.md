# Explicação Simples das Classes do Sistema (Como se Você Fosse Burro 😄)

Ei! Vou explicar **cada classe** desse sistema de forma **MUITO SIMPLES**, como se você nunca tivesse visto código antes. Imagine que cada classe é uma **pessoa com um trabalho específico** no time que lê informações escondidas nas fotos de drone (metadados como GPS, altitude, etc.).

O sistema todo serve pra **abrir fotos de drone, pegar TODAS as informações técnicas** (onde foi tirada, altura do drone, ângulo da câmera, etc.) e organizar num dicionário bonitinho pra usar em mapas ou análises.

## 1. **ExifUtil** (o "Leitor de Etiquetas Básicas")
   - **O que faz?** É como um detetive que olha 3 lugares diferentes em cada foto:
     1. **Sistema do Windows** (nome do arquivo, tamanho, quando foi salva)
     2. **Propriedades da imagem** (largura/altura em pixels, formato JPG/PNG)
     3. **EXIF** (dados da câmera: data da foto, ISO, velocidade do obturador)
   - **Como usar?** `ExifUtil.extract_metadata_os("foto.jpg")` → devolve dict com basics
   - **Por que existe?** Fotos têm essas infos "escondidas". Ele acha tudo rapidinho.
   - **Exemplo simples:** Abre foto → "Ah, tem 5MB, 1920x1080 pixels, tirada em 2024-01-01 14:30"

## 2. **XmpUtil** (o "Especialista em Drones DJI")
   - **O que faz?** Lê o **XML especial dos drones DJI** (XMP). É onde tá o ouro: 
     - Altitude do drone (absoluta e relativa)
     - Posição GPS, yaw/pitch/roll do gimbal e drone
     - Velocidades de voo (X/Y/Z), RTK (precisão GPS), número de fotos tiradas
     - Serial do drone/câmera, UUID da captura
   - **Como usar?** `XmpUtil.extract_metadata("foto.jpg")` → dict com tudo do drone
   - **Por que existe?** Drones DJI guardam dados TOP aí. Sem isso, você só tem data/hora básica.
   - **Exemplo:** "Drone voava a -14m/s em X, altitude 542m, gimbal apontado -89° pra baixo"

## 3. **Manager** (o "Chefe que Junta Tudo")
   - **O que faz?** É o **maestro**:
     1. Chama ExifUtil + XmpUtil pra cada foto
     2. Pega só os **campos importantes** (definidos em Strings.REQUIRED_FIELDS)
     3. Se você der uma pasta, processa **TODAS as fotos** e devolve dict gigante { "foto1.jpg": {dados}, "foto2.jpg": {dados} }
   - **Como usar?** `Manager.collect_metadata("pasta_com_fotos/")` → tudo organizado!
   - **Por que existe?** Sem ele, você teria que chamar 4 classes manualmente. Ele simplifica.
   - **Exemplo:** Dá pasta → recebe 100 fotos com GPS/altitude/velocidade cada.

## 4. **Strings** (o "Livro de Regras")
   - **O que faz?** É só um **dicionário gigante** (REQUIRED_FIELDS) que diz:
     - Quais campos pegar de cada fonte (EXIF, XMP, OS)
     - Nome "bonitinho" pra cada (ex: "GPSMapDatum" vem de "EXIF:GPSInfo:GPSMapDatum")
     - Descrição de cada campo ("Datum da foto", "Velocidade do obturador")
   - **Como usar?** Manager usa automaticamente `Strings.REQUIRED_FIELDS`
   - **Por que existe?** Pra todo mundo usar os **mesmos nomes e campos**. Sem bagunça.
   - **Exemplo:** 60+ campos padronizados (file, path, Model, AbsoluteAltitude, RtkFlag...)

## Como o Sistema Funciona no Geral? (Passo a Passo BURRO)
```
1. Você roda main.py
2. Manager recebe "pasta_de_fotos/"
3. Manager lista todas JPG
4. Pra cada foto:
   → ExifUtil pega basics + EXIF
   → XmpUtil pega dados DJI
   → Manager filtra pelos campos de Strings
5. Você recebe: {"foto1.jpg": {60 campos}, "foto2.jpg": {...}}
```

**Resumo Ultra-Burro:**
- **ExifUtil**: basics da foto
- **XmpUtil**: mágica do drone
- **Manager**: junta e filtra
- **Strings**: lista do que pegar

Agora você entende TUDO! Rode `python main.py "sua_pasta"` e veja a mágica. 🚁📸✨

