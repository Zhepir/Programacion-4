from datetime import date

import nh3

from rest_framework import serializers

from .models import Project, Task, Tag
from .services import HolidayService


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    due_on_holiday = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "title",
            "description",
            "priority",
            "status",
            "due_date",
            "due_on_holiday",
            "tags",
            "created_at",
        ]

    def get_due_on_holiday(self, obj):
        if not obj.due_date:
            return False
        return HolidayService.is_holiday(obj.due_date)

    def validate_due_date(self, value):
        if value and value < date.today():
            raise serializers.ValidationError(
                "La fecha límite no puede ser en el pasado."
            )
        return value

    def validate_description(self, value):
        return nh3.clean(value, tags=set())


    def validate(self, data):
        # En un PATCH, "data" trae solo los campos enviados.
        # Lo que falte lo tomamos de la instancia existente.
        instance = self.instance

        status = data.get(
            "status",
            instance.status if instance else None
        )

        due_date = data.get(
            "due_date",
            instance.due_date if instance else None
        )

        project = data.get(
            "project",
            instance.project if instance else None
        )

        # Regla de la Clase 4
        if status == "completada" and not due_date:
            raise serializers.ValidationError(
                "No se puede marcar una tarea como completada sin fecha límite registrada."
            )

        # Tarea para la casa
        if status == "en_progreso":
            hay_completadas = project.tasks.filter(
                status="completada"
            ).exists()

            if not hay_completadas:
                raise serializers.ValidationError(
                    "No se puede pasar a 'en_progreso' una tarea de un proyecto "
                    "que todavía no tiene ninguna tarea completada."
                )

        return data


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "tasks",
            "created_at",
        ]


#---------------------------------------------------------
