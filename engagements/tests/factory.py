import factory
from django.contrib.auth.models import User
from engagements.models import Engagement, EngagementTopic
from projects.models import Project
from stakeholders.models import Stakeholder, StakeholderOrg
from ppdds.models import PPDD


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class EngagementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Engagement

    user = factory.SubFactory(UserFactory)
    date = factory.Faker('date')
    summary = factory.Faker('text')
    project = Project.objects.create(name='Test Project')
    stakeholder = Stakeholder.objects.create(
        first_name='Terry',
        last_name='Jacks',
        organisation=StakeholderOrg.objects.create(name='DfT(c)'),
    )
    ppdd = PPDD.objects.create(first_name='Jimmy', last_name='Jones')
    topic = EngagementTopic.objects.create(topic='Test Topic')

    Engagement.objects.create(
        user=user,
        date=date.today(),
        summary='Test Summary'
    )
    engagement = Engagement.objects.first()
    engagement.projects.add(project)
    engagement.stakeholders.add(stakeholder)
    engagement.ppdds.add(ppdd)
    engagement.topics.add(topic)