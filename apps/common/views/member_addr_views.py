from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from common.models.location_model import Location
from common.models.member_addr_model import Memberaddr
from common.serializers.member_serializer import memberAddrSerializer
from common.views.schema.member_addr_schema import member_addr_schema_create, member_addr_example, member_addr_schema, \
	member_addr_example_create, member_addr_schema_update, member_addr_example_update
from common.forms.member_addr_form import MemberAddrForm
from common.forms.member_addr_form import MemberAddrNonDistanceForm


@swagger_auto_schema(method='delete', request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT,
		properties=member_addr_schema,
		example=member_addr_example,
		required=['addr']
		),
        operation_id='member_addr_delete',
		responses={
			204: 'Delete member address completed.'
		})
@api_view(['GET', 'DELETE'])
def member_addr(request, id_member):
	"""
	특정멤버의 주소 조회, 삭제

	---

	"""
    memberAddr = Memberaddr.objects.filter(id_member=id_member)
    if memberAddr.count() == 0:
        content = {
            "message": "사용자가 설정한 주소가 없습니다.",
            "result": {}
        }
        return Response(content, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = memberAddrSerializer(memberAddr, many=True)
        return Response(serializer.data)

	elif request.method == 'DELETE':
		Addr = request.data['addr']
		# 1개인 경우 삭제 불가
		if memberAddr.count() <= 1:
			content = {
				"message": "동네가 1개만 선택된 상태에서는 삭제를 할 수 없습니다.",
				"result": {"addr": Addr}
			}
			return Response(content, status=status.HTTP_202_ACCEPTED)
		# 삭제
		q = memberAddr.get(addr=Addr)
		q.delete()
		# 다른 주소는 Y로 변경
		Memberaddr.objects.filter(id_member=id_member).update(select="Y")
		content = {
			"message": "삭제 완료",
			"result": {"addr": Addr}
		}
		return Response(content, status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT,
		properties=member_addr_schema_create,
		example=member_addr_example_create,
		required=['id_member', 'addr']
		),
        operation_id='member_addr_create',
		responses={
			201: 'Member Address Registration Completed.'
		})
@api_view(['POST'])
def member_addr_create(request):
	"""
	특정멤버 주소 생성

	---

	"""
    if request.method == 'POST':
        Data = request.body.decode('utf-8')
        received_json_data = json.loads(Data)
        received_json_data['id_member'] = request.headers['id-member']
        Person = Memberaddr.objects.filter(id_member=received_json_data['id_member'])
        # 주소 유효성 검사
        form = MemberAddrNonDistanceForm(received_json_data)
        if form.is_valid():
            # Case 1. 주소가 0개인 회원
            if Person.count() == 0:
                form.save()
                content = {
                    "message": "등록 완료",
                    "result": {
                        "등록된 주소 : " + form.cleaned_data['addr']
                    }
                }
                return Response(content, status=status.HTTP_201_CREATED)
            # Case 2. 주소가 1개인 회원
            elif Person.count() == 1:
                # 중복체크
                if form.user_addr():
                    content = {
                        "message": "중복된 주소가 있습니다.",
                        "result": {"입력 받은 주소 : " + form.cleaned_data['addr']}
                    }
                    return Response(content, status=status.HTTP_409_CONFLICT)
                # 중복 없을 때
                else:
                    # 기존에 있던 주소의 선택사항은 "선택안함"
                    Person.update(select="N")
                    # 새로운 주소 등록
                    form.save()
                    content = {
                        "message": "등록 완료",
                        "result": {
                             "등록된 주소 : " + form.cleaned_data['addr']
                        }
                    }
                    return Response(content, status=status.HTTP_201_CREATED)
            elif Person.count() >= 2:
                content = {
                    "message": "허용된 주소의 갯수는 2개입니다.",
                    "result": {}
                }
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                "message": form.errors.as_data(),
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=openapi.Schema(
		type=openapi.TYPE_OBJECT,
		properties=member_addr_schema_update,
		example=member_addr_example_update,
		required=['addr', 'dis']
		),
		responses={
			200: 'Select member address & Set distance.'
		})
@api_view(['PUT'])
def member_addr_dis_update(request):
    """
	특정멤버 주소 선택 & 거리 견경

	---

	"""

    id_member = request.headers["id-member"]
    Data = json.loads(request.body)
    member = Memberaddr.objects.filter(id_member=id_member)
    addr = Data['addr']
    dis = Data['dis']

    data = {
        "id_member": id_member,
        "addr": addr,
        "distance": dis
    }
    form = MemberAddrForm(data)
    # 유효성 검사
    if form.is_valid():
        if not(form.user_addr()):
            content = {
                "message": "등록되지 않은 주소입니다",
                "result": {}
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        member.update(select="N")
        addrselect = member.get(addr=form.cleaned_data['addr'])
        addrselect.select = "Y"
        addrselect.distance = form.cleaned_data['distance']
        addrselect.save()
        content = {
            "message": "수정완료",
            "result": {
                "select_addr": form.cleaned_data['addr'],
                "distance": form.cleaned_data['distance']
            }
        }
        return Response(content, status=status.HTTP_200_OK)

    else:
        content = {
            "message": form.errors.as_data(),
            "result": {}
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
