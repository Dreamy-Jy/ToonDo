import graphene
from graphene_django import DjangoObjectType
from .models import Todo

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info, **kwargs):
        return Todo.objects.all()

class CreateTodo(graphene.Mutation):
    id = graphene.Int()
    complete = graphene.Boolean()
    title = graphene.String() 
    
    class Arguments:
        title = graphene.String()
    
    # TODO add code to process titles that are to large 
    def mutate(self, info, title):
        todo = Todo(title=title)
        todo.save()

        return CreateTodo(
            id=todo.id,
            title=todo.title,
            complete=todo.complete
        )

class RemoveTodo(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    complete = graphene.Boolean()

    # TODO add support for searching for todos through other properties
    class Arguments:
        id = graphene.Int()
    
    # TODO add error handling for non-existing id
    # NOTE once a todo is deleted it's id becomes null
    def mutate(self, info, id):
        todo = Todo.objects.get(id=id)
        todo.delete()

        return RemoveTodo(
            id=todo.id,
            title=todo.title,
            complete=todo.complete
        )    

class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    remove_todo = RemoveTodo.Field()
        
