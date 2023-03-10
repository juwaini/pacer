from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from score.models import Score


def get_score(request, pk):
    try:
        data = Score.objects.get(user=pk)
        r = {'success': True, 'id': data.user.pk, 'score': data.score}
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)


def get_score_divided(request, pk):
    try:
        data = Score.objects.get(user=pk)
        r = {'success': True, 'id': data.user.pk, 'score': data.score_divided}
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)


@csrf_exempt
def set_score(request, pk):
    print(request.POST)
    try:
        data = Score.objects.get(user=pk)
        data.score = request.POST['score']
        data.score_divided = int(request.POST['score'])/2
        data.save()
        r = {
            'message': f'score for user {data.user.pk} successfully edited.',
            'success': True,
            'id': data.user.pk,
            'score': data.score,
        }
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)
