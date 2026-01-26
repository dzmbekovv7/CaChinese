from django.core.management.base import BaseCommand
from ...models import Grammar, GrammarQuestion

class Command(BaseCommand):
    help = "Seed grammar data for HSK 1 and HSK 2"

    def handle(self, *args, **kwargs):
        grammar1 = Grammar.objects.create(
            title="是 (shì) – basic sentence structure",
            description="是 is used to connect the subject with a noun or pronoun. It means 'to be'.",
            example="我是学生。",
            hsk_level=1
        )

        GrammarQuestion.objects.create(
            grammar=grammar1,
            question_text="Choose the correct sentence:",
            question_type="mcq",
            options=["我是老师。", "我老师是。", "我老师。"],
            correct_answer="我是老师。"
        )

        GrammarQuestion.objects.create(
            grammar=grammar1,
            question_text="是 can be used between two nouns.",
            question_type="tf",
            correct_answer="True"
        )

        # HSK 2 – 了
        grammar2 = Grammar.objects.create(
            title="了 (le) – completed action",
            description="了 is used after a verb to show that an action has been completed.",
            example="我吃了饭。",
            hsk_level=2
        )

        GrammarQuestion.objects.create(
            grammar=grammar2,
            question_text="我看___电影。",
            question_type="fill",
            correct_answer="了"
        )

        GrammarQuestion.objects.create(
            grammar=grammar2,
            question_text="Which sentence shows a completed action?",
            question_type="mcq",
            options=["我吃饭。", "我吃了饭。", "我吃饭了？"],
            correct_answer="我吃了饭。"
        )

        self.stdout.write(self.style.SUCCESS("Grammar data seeded successfully!"))
