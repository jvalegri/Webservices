import csv
import xml.etree.ElementTree as ET

def criar_curso(curso_id, nome, coordenador, disciplinas):
    curso = ET.SubElement(root, "curso", id=str(curso_id))
    coord = ET.SubElement(curso, "coordenador")
    ET.SubElement(coord, "nome").text = coordenador[0]
    ET.SubElement(coord, "matricula").text = str(coordenador[1])
    ET.SubElement(coord, "email").text = coordenador[2]
    disciplinas_elem = ET.SubElement(curso, "disciplinas")
    for disciplina in disciplinas:
        disc = ET.SubElement(disciplinas_elem, "disciplina")
        ET.SubElement(disc, "codigo").text = disciplina[0]
        ET.SubElement(disc, "nome").text = disciplina[1]
        ET.SubElement(disc, "cargaHoraria").text = str(disciplina[2])

# Criando a estrutura raiz do XML
root = ET.Element("cursos")

# Lendo os dados do CSV (ajuste o caminho do arquivo e o delimitador se necessário)
with open('/home/jvalegri/Documentos/cursos.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Pula o cabeçalho
    for row in reader:
        curso_id, nome, coordenador_nome, matricula, email, codigo_disciplina, nome_disciplina, carga_horaria = row
        coordenador = (coordenador_nome, matricula, email)
        disciplinas = [(codigo_disciplina, nome_disciplina, carga_horaria)]
        criar_curso(curso_id, nome, coordenador, disciplinas)

# Criando o arquivo XML
tree = ET.ElementTree(root)
with open("cursos1.xml", "wb") as arquivo:
    tree.write(arquivo, encoding='utf-8', xml_declaration=True)