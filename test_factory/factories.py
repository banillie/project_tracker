import factory
from django.contrib.auth.models import User
from engagements.models import Engagement, EngagementTopic
from projects.models import Tier, Stage, Type, Project
from stakeholders.models import DFTGroup, Stakeholder, StakeholderOrg
from ppdds.models import PPDD

class GenericModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    name = factory.Faker('word')

class TierFactory(GenericModelFactory):
    class Meta:
        model = Tier

class StageFactory(GenericModelFactory):
    class Meta:
        model = Stage

class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    type = factory.Faker('word')

class DfTGroupFactory(GenericModelFactory):
    class Meta:
        model = DFTGroup

class StakeholderOrgFactory(GenericModelFactory):
    class Meta:
        model = StakeholderOrg

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.Sequence(lambda n: f'user{n}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password123')

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    user = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: f'Project {n}')
    type = 'Type'
    sort = factory.SubFactory(TypeFactory)
    abbreviation = factory.Sequence(lambda n: f'ABBR{n}')
    governance = 'Governance'
    dft_group = factory.SubFactory(DfTGroupFactory)
    tier = factory.SubFactory(TierFactory)
    stage = 'Stage'
    stage_name = factory.SubFactory(StageFactory)
    scope = factory.Faker('text', max_nb_chars=2000)
    live = True
    

class StakeholderFactory():
    class Meta:
        model = Stakeholder

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    # slug = factory.Sequence(lambda n: f'stakeholder-{n}')
    organisation = factory.SubFactory(StakeholderOrgFactory)
    group = factory.Faker('word')
    dft_group = factory.SubFactory(DfTGroupFactory)
    team = factory.Faker('word')
    role = factory.Faker('word')
    tele_no = factory.Faker('phone_number')
    live = True
    my_dft_url = factory.Faker('url')


class EngagementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Engagement

    user = factory.SubFactory(UserFactory)
    date = factory.Faker('date')
    summary = factory.Faker('text')
    projects = factory.SubFactory(ProjectFactory)
    # projects = factory.SubFactoryList(ProjectFactory, size=1)  # Adjust size as needed
    # stakeholders = factory.SubFactoryList(StakeholderFactory, size=1)

    # project = Project.objects.create(name='Test Project')
    # stakeholder = Stakeholder.objects.create(
    #     first_name='Terry',
    #     last_name='Jacks',
    #     organisation=StakeholderOrg.objects.create(name='DfT(c)'),
    # )
    # ppdd = PPDD.objects.create(first_name='Jimmy', last_name='Jones')
    # topic = EngagementTopic.objects.create(topic='Test Topic')
    #
    # Engagement.objects.create(
    #     user=user,
    #     date=date.today(),
    #     summary='Test Summary'
    # )
    # engagement = Engagement.objects.first()
    # engagement.projects.add(project)
    # engagement.stakeholders.add(stakeholder)
    # engagement.ppdds.add(ppdd)
    # engagement.topics.add(topic)