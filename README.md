# EDA-QuadTree

## Contexto: 

É inquestionável a aplicação de estruturas do tipo árvore em diversas áreas conforme visto em aula. Pensando nisso, você deverá desenvolver alguns métodos baseados na QuadTree apresentada em aula.

Classe abstrata: Use a classe abstrata a seguir e isso significa que não deverá ser alterado nenhum nome de método. Lembre-se que, para a validação de cada método, o professor utiliza testes automatizados e, portanto, é fundamental que não seja alterado nada.

**Passo 1)** Crie a seguinte classe abstrata e vincule-a à classe QuadTree apresentada em aula.

```
class QuadTreeADT(ABC):

@abstractmethod
def clear(self) -> None: ...

@abstractmethod
def is_empty(self) -> bool: ...

@abstractmethod
def insert(self, x: object, y: object, value: object) -> None: ...

@abstractmethod
def query_2D(self, rect: Interval2D) -> None: ...

@abstractmethod
def search(self, point: Point) -> object: ...

@abstractmethod
def all_points(self) -> List[Point]: ...
```

**Passo 2)** Desenvolva cada método destacado em azul conforme regra de negócio descrita no Quadro 1.
Lembre-se que poderá ser criado qualquer método que facilite o desenvolvimento.

**Quadro 1:** Descrição dos Contratos

| Contrato | Objetivo | Parametros | Retorno |
| -------- | -------- | ---------- | ------- |
| search | Retornar o valor associado à coordenada. | point: coordenada em forma de objeto do tipo Point. Você deverá criar a classe Point (colocar dentro do arquivo QuadTree). | Valor associado com a coordenada ou None (caso não encontrada). |
| all_points | Retornar uma lista com todas as coordenadas em forma de objeto Point. | Sem parâmetro. | Lista com todas as coordenadas em forma de objeto Point ou None (caso não exista coordenada). |


## Organização
- NÃO SERÁ ACEITO A ENTREGA DO TRABALHO INDIVIDUALMENTE, POIS A ATIVIDADE É EM
GRUPO

- Para a entrega, somente um do grupo precisa submetê-lo no EAD. Exporte um arquivo formato ZIP
com o seguinte nome: aluno1_aluno2_trabalhofinal.zip, contendo o código do projeto

- Código o mais claro possível, seguindo boas práticas de nomenclatura e estrutura

- Não será aceito a entrega (via Moodle) do trabalho após a data limite

- Não será aceito trabalho igual ao de outros colegas. Esta prática é chamada de plágio. Inclusive, será verificado se o código foi desenvolvido usando LLMs (e.g. ChatGPT)
