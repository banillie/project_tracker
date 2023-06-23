import factory
from django.contrib.auth.models import User
from engagements.models import Engagement, EngagementTopic
from projects.models import Tier, Stage, Type, Project, TYPE_CHOICES
from stakeholders.models import DFTGroup, Stakeholder, StakeholderOrg
from ppdds.models import PPDD, PPDDDivison

class GenericModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        abstract = True

    name = factory.Faker('word')

class TierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tier

    type = factory.Faker('word')

class StageFactory(GenericModelFactory):
    class Meta:
        model = Stage

class EngagementTopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EngagementTopic

    topic = factory.Faker('word')

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

class PPDDDivisonFactory(GenericModelFactory):
    class Meta:
        model = PPDDDivison

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
    type = factory.Iterator([choice[1] for choice in TYPE_CHOICES])
    # sort = factory.SubFactory(TypeFactory)
    abbreviation = factory.Sequence(lambda n: f'ABBR{n}')
    governance = 'Governance'
    dft_group = factory.SubFactory(DfTGroupFactory)
    tier = factory.SubFactory(TierFactory)
    stage = 'Stage'
    stage_name = factory.SubFactory(StageFactory)
    scope = factory.Faker('text', max_nb_chars=2000)
    live = True
    
class StakeholderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stakeholder

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    organisation = factory.SubFactory(StakeholderOrgFactory)
    group = factory.Faker('word')
    dft_group = factory.SubFactory(DfTGroupFactory)
    team = factory.Faker('word')
    role = factory.Faker('word')
    tele_no = factory.Faker('phone_number')
    live = True
    my_dft_url = factory.Faker('url')

class PPDDFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PPDD

    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    slug = factory.Sequence(lambda n: f'slug{n}')
    team = factory.Faker('word')
    division = factory.SubFactory(PPDDDivisonFactory)
    role = factory.Faker('job')
    tele_no = factory.Faker('phone_number')
    live = True

class EngagementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Engagement

    user = factory.SubFactory(UserFactory)
    date = factory.Faker('date_object')
    summary = factory.Faker('text', max_nb_chars=2000)

    @factory.post_generation
    def create_projects(self, create, extracted, **kwargs):
        # Always create a project using ProjectFactory
        project = ProjectFactory()
        self.projects.add(project)
        
        # Use the ProjectFactory to create a list of projects
        # projects = ProjectFactory.create_batch(3)
        # for project in projects:
        #     self.projects.add(project)

    @factory.post_generation
    def create_stakeholders(self, create, extracted, **kwargs):
        stakeholder = StakeholderFactory()
        self.stakeholders.add(stakeholder)

    @factory.post_generation
    def create_ppdds(self, create, extracted, **kwargs):
        ppdd = PPDDFactory()
        self.ppdds.add(ppdd)

    @factory.post_generation
    def create_topics(self, create, extracted, **kwargs):
        topic = EngagementTopicFactory()
        self.topics.add(topic)
