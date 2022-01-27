from rest_framework.viewsets import ModelViewSet
from main.models import Person
from main.api.serializers import PersonSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import (
    date,
    datetime
)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def create(self, request, *args, **kwargs):
        iin = request.data['iin']
        today = datetime.today()
        birth_date = datetime.strptime(iin[:6], '%y%m%d')

        if birth_date.year > datetime.today().year:
            birth_date = datetime.strptime(str(birth_date.year - 100) + str(birth_date.month) + str(birth_date.day),
                                           '%Y%m%d')

        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        data = {
            'iin': iin,
            'age': age
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
