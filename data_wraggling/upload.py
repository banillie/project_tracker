import datetime
import os
import json

from project_tracker.settings import ROOT_DIR
from engagements.models import (
    Engagement,
    EngagementType,
    EngagementWorkStream,
    EngagementTopic,
)
from projects.models import Project
from stakeholders.models import Stakeholder, StakeholderOrg
from ppdds.models import PPDD

from openpyxl import load_workbook, Workbook


# def upload_data():
#     data_path = os.path.join(ROOT_DIR, 'project_tracker/data/project_tracker_data.xlsx')
#     wb = load_workbook(data_path)
#
#     # Stakeholders
#     ws = wb["Stakeholders"]
#     org_list = []
#     for row in range(2, ws.max_row+1):
#         org = ws.cell(row=row, column=3).value
#         if org not in org_list:
#             org_list.append(org)
#         else:
#             pass
#
#     for x in org_list:
#         StakeholderOrg.objects.create(name=x)
#
#     all_entries = {}
#     for row in range(2, ws.max_row+1):
#         single_entry = {}
#         single_entry["first_name"] = ws.cell(row=row, column=1).value.strip()
#         # using strip to tidy string whitespacing
#         single_entry["last_name"] = ws.cell(row=row, column=2).value.strip()
#         org = ws.cell(row=row, column=3).value
#         single_entry["organisation"] = StakeholderOrg.objects.get(name=org)
#         single_entry["group"] = ws.cell(row=row, column=4).value
#         single_entry["team"] = ws.cell(row=row, column=5).value
#         single_entry["role"] = ws.cell(row=row, column=6).value
#         single_entry["tele_no"] = ws.cell(row=row, column=7).value
#         all_entries[int(row)] = single_entry
#
#     for x in all_entries:
#         Stakeholder.objects.create(
#             **all_entries[x],
#         )
#
#     # PPDD data
#     ws = wb['PPDDs']
#     all_entries = {}
#     for row in range(2, ws.max_row+1):
#         single_entry = {}
#         single_entry["first_name"] = ws.cell(row=row, column=1).value.strip()
#         single_entry["last_name"] = ws.cell(row=row, column=2).value.strip()
#         single_entry["role"] = ws.cell(row=row, column=3).value
#         single_entry["team"] = ws.cell(row=row, column=4).value
#         single_entry["tele_no"] = ws.cell(row=row, column=5).value
#         all_entries[int(row)] = single_entry
#
#     for x in all_entries:
#         PPDD.objects.create(
#             **all_entries[x],
#         )
#
#     # Project data
#     ws = wb['Projects']
#
#     all_entries = {}
#     for row in range(2, ws.max_row+1):
#         single_entry = {}
#         single_entry["name"] = ws.cell(row=row, column=2).value
#         single_entry["type"] = ws.cell(row=row, column=1).value
#         single_entry["abbreviation"] = ws.cell(row=row, column=3).value
#         single_entry["governance"] = ws.cell(row=row, column=4).value
#         all_entries[int(row)] = single_entry
#
#     for x in all_entries:
#         Project.objects.create(
#             **all_entries[x],
#         )
#
#     # Engagement data
#     ws = wb['EngagementTypes']
#     type_list = []
#     for row in range(2, ws.max_row+1):
#         type = ws.cell(row=row, column=1).value
#         if type:
#             if type not in type_list:
#                 type_list.append(type)
#             else:
#                 pass
#         else:
#             pass
#
#     for x in type_list:
#         EngagementTopic.objects.create(topic=x)
#
#     # wsheet = wb['EngagementWorkStreams']
#     # ws_list = []
#     # for row in range(2, wsheet.max_row+1):
#     #     ws = wsheet.cell(row=row, column=1).value
#     #     if ws not in ws_list:
#     #         ws_list.append(ws)
#     #     else:
#     #         pass
#     #
#     # for x in ws_list:
#     #     EngagementWorkStream.objects.create(work_stream=x)
#
#     ws = wb['Engagements']
#     for row in range(2, ws.max_row+1):
#         eng = Engagement(
#             date=ws.cell(row=row, column=1).value,
#             summary=ws.cell(row=row, column=7).value,
#
#         )
#         eng.save()
#
#         project_list = ws.cell(row=row, column=2).value.split(", ")
#         p_object_list = []
#         for name in project_list:
#             p_object_list.append(Project.objects.get(name=name))
#         eng.projects.add(*p_object_list)
#
#         stakeholder_list = ws.cell(row=row, column=4).value.split(", ")
#         object_list = []
#         for name in stakeholder_list:
#             split_name = name.split(" ")
#             object_list.append(Stakeholder.objects.get(
#                 first_name=split_name[0],
#                 last_name=split_name[1])
#             )
#         eng.stakeholders.add(*object_list)
#
#         ppdd_list = ws.cell(row=row, column=3).value.split(", ")
#         object_list = []
#         for name in ppdd_list:
#             split_name = name.split(" ")
#             object_list.append(PPDD.objects.get(
#                 first_name=split_name[0],
#                 last_name=split_name[1])
#             )
#         eng.ppdds.add(*object_list)
#
#         type_list = ws.cell(row=row, column=5).value.split(", ")
#         type_object_list = []
#         for type in type_list:
#             print()
#             type_object_list.append(EngagementTopic.objects.get(topic=type))
#         eng.topics.add(*type_object_list)
#
#         # wstream = ws.cell(row=row, column=6).value
#         # if wstream:
#         #     ws_list = wstream.value.split(", ")
#         #     ws_object_list = []
#         #     for x in ws_list:
#         #         ws_object_list.append(EngagementWorkStream.objects.get(work_stream=x))
#         #     eng.engagement_workstreams.add(*ws_object_list)
#         # else:
#         #     pass
#
#
# def test_merge_worktype_with_workstream() -> None:
#     # code of merging fields 'engagement_workstream' and 'engagement_type' into the
#     # newly created 'topics' field in Engagement model.
#     for engagement in Engagement.objects.all():
#         if engagement.engagement_types is not None:
#             for type in engagement.engagement_types.all():
#                 topic, created = EngagementTopic.objects.get_or_create(topic=type.type)
#                 engagement.topics.add(EngagementTopic.objects.get(topic=topic))
#         if engagement.engagement_workstreams is not None:
#             for ws in engagement.engagement_workstreams.all():
#                 topic, created = EngagementTopic.objects.get_or_create(topic=ws.work_stream)
#                 engagement.topics.add(EngagementTopic.objects.get(topic=topic))

#
# def open_json_file(path: str):
#     with open(path, "r") as handle:
#         return json.load(handle)


def excel_download(output: str) -> None:
    wb = Workbook()

    ws = wb.create_sheet("Engagements")  # Engagement output
    fields_all = [f.name for f in Engagement._meta.get_fields()]
    # remove = ['id',
    #           'user'
    #           ] # fields currently not required for user
    # fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields_all):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(Engagement.objects.all().order_by('-date')):  # order by date
            v = getattr(p, f)
            try:
                if f == 'user':
                    ws.cell(row=i + 2, column=x + 1).value = str(v)
                else:
                    ws.cell(row=i + 2, column=x + 1).value = v
                    if isinstance(v, datetime.date):
                        ws.cell(row=i + 2, column=x + 1).number_format = "dd/mm/yy"
            except ValueError:
                m2m_list = []
                attribute_list = v.all()  # for many-to-many model instance fields.
                for y in attribute_list:
                    m2m_list.append(str(y))
                ws.cell(row=i + 2, column=x + 1).value = ', '.join(m2m_list)

    ws = wb.create_sheet("Projects")  # Project output
    fields_all = [f.name for f in Project._meta.get_fields()]
    remove = [
        "engagement",
        # "id",
        # "user",
        "slug",
        "governance",
        "stage",
        "live",
        "timestamp",
        "updated",
    ]  # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(Project.objects.all()):
            val = getattr(p, f)
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                if val is not None:
                    ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))
                else:
                    ''

    ws = wb.create_sheet("Stakeholders")  # Stakeholder output
    fields_all = [f.name for f in Stakeholder._meta.get_fields()]
    remove = ['engagement',
              # 'id',
              'user',
              'slug',
              'group',
              'live'] # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(Stakeholder.objects.all().order_by('last_name')):
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))

    ws = wb.create_sheet("PPDD")  # PPDD output
    fields_all = [f.name for f in PPDD._meta.get_fields()]
    remove = ['engagement',
              # 'id',
              'user',
              'slug',
              'tele_no',
              'live']  # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(PPDD.objects.all().order_by('last_name')):
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))

    wb.remove(wb["Sheet"])

    wb.save(output)


def excel_download_pbi(output: str) -> None:
    wb = Workbook()
    ws = wb.create_sheet("Engagements")  # Engagement output

    e_qs = Engagement.objects.raw(
        'SELECT * FROM engagements_engagement'
    )
    for x, f in enumerate(e_qs):
        ws.cell(row=x + 2, column=1).value = f.id
        ws.cell(row=x + 2, column=2).value = f.date
        ws.cell(row=x + 2, column=2).number_format = "dd/mm/yy"

    ws.cell(row=1, column=1).value = 'ENGAGEMENT_ID'
    ws.cell(row=1, column=2).value = 'DATE'


    ## Different method. Keep in case useful to refer to later
    # fields_all = [f.name for f in Engagement._meta.get_fields()]
    # remove = [
    #     # 'id',
    #     'user',
    #     'projects',
    #     'stakeholders',
    #     'ppdds',
    #     'topics',
    #     'summary',
    #     ]
    # fields = [x for x in fields_all if x not in remove]
    # for x, f in enumerate(fields):
    #     ws.cell(row=1, column=x + 1).value = f.upper()
    #     for i, p in enumerate(Engagement.objects.all().order_by('-date')):  # order by date
    #         try:
    #             ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
    #             if isinstance(getattr(p, f), datetime.date):
    #                 ws.cell(row=i + 2, column=x + 1).number_format = "dd/mm/yy"
    #         except ValueError:
    #             m2m_list = []
    #             attribute_list = getattr(p, f).all()  # for many-to-many model instance fields.
    #             for y in attribute_list:
    #                 m2m_list.append(str(y))
    #             ws.cell(row=i + 2, column=x + 1).value = ', '.join(m2m_list)

    ws = wb.create_sheet('Engagement_Topics')
    et_qs = Engagement.objects.raw(
        'SELECT * FROM engagements_engagement_topics'
    )
    for x, f in enumerate(et_qs):
        ws.cell(row=x + 2, column=1).value = f.id
        ws.cell(row=x + 2, column=2).value = f.engagement_id
        ws.cell(row=x + 2, column=3).value = f.engagementtopic_id
        ws.cell(row=x + 2, column=4).value = str(EngagementTopic.objects.get(id=f.engagementtopic_id))

    ws.cell(row=1, column=1).value = 'ID'
    ws.cell(row=1, column=2).value = 'ENGAGEMENT ID'
    ws.cell(row=1, column=3).value = 'ENGAGEMENT_TOPIC ID'
    ws.cell(row=1, column=4).value = 'ENGAGEMENT_TOPIC NAME'

    ws = wb.create_sheet('Engagement_Projects')
    ep_qs = Engagement.objects.raw(
        'SELECT * FROM engagements_engagement_projects'
    )
    for x, ep in enumerate(ep_qs):
        ws.cell(row=x + 2, column=1).value = ep.id
        ws.cell(row=x + 2, column=2).value = ep.engagement_id
        ws.cell(row=x + 2, column=3).value = ep.project_id
        instance = Project.objects.get(id=ep.project_id)
        ws.cell(row=x + 2, column=4).value = str(instance)
        ws.cell(row=x + 2, column=5).value = str(instance.tier)
        ws.cell(row=x + 2, column=6).value = str(instance.type)
        ws.cell(row=x + 2, column=7).value = str(instance.dft_group)


    ws.cell(row=1, column=1).value = 'ID'
    ws.cell(row=1, column=2).value = 'ENGAGEMENT ID'
    ws.cell(row=1, column=3).value = 'PROJECT ID'
    ws.cell(row=1, column=4).value = 'PROJECT NAME'
    ws.cell(row=1, column=5).value = 'PROJECT TIER'
    ws.cell(row=1, column=6).value = 'PROJECT TYPE'
    ws.cell(row=1, column=7).value = 'PROJECT GROUP'

    ws = wb.create_sheet("Projects")  # Project output
    fields_all = [f.name for f in Project._meta.get_fields()]
    remove = [
        "engagement",
        # "id",
        "user",
        "slug",
        "governance",
        "stage",
        "live",
        "timestamp",
        "updated",
        "scope"
    ]  # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(Project.objects.all()):
            val = getattr(p, f)
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                if val is not None:
                    ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))
                else:
                    ''

    ws = wb.create_sheet("Stakeholders")  # Stakeholder output
    fields_all = [f.name for f in Stakeholder._meta.get_fields()]
    remove = ['engagement',
              'id',
              'user',
              'slug',
              'group',
              'live'] # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(Stakeholder.objects.all().order_by('last_name')):
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))

    ws = wb.create_sheet("PPDD")  # PPDD output
    fields_all = [f.name for f in PPDD._meta.get_fields()]
    remove = ['engagement',
              'id',
              'user',
              'slug',
              'tele_no',
              'live']  # fields currently not reqired for user
    fields = [x for x in fields_all if x not in remove]

    for x, f in enumerate(fields):
        ws.cell(row=1, column=x + 1).value = f.upper()
        for i, p in enumerate(PPDD.objects.all().order_by('last_name')):
            try:
                ws.cell(row=i + 2, column=x + 1).value = getattr(p, f)
            except ValueError:
                ws.cell(row=i + 2, column=x + 1).value = str(getattr(p, f))

    wb.remove(wb["Sheet"])

    wb.save(output)
