from django.http import JsonResponse

from score.models import Score


def get_score(request, pk):
    try:
        data = Score.objects.get(user=pk)
        r = {'success': True, 'id': data.user.pk, 'score': data.score * 2}
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)


def get_score_divided(request, pk):
    try:
        data = Score.objects.get(user=pk)
        r = {'success': True, 'id': data.user.pk, 'score': data.score / 2}
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)


def set_score(request, pk):
    try:
        data = Score.objects.get(user=pk)
        data.score = request.POST['score']
        data.save()
        r = {
            'message': f'score for user {data.user.pk} successfully edited.',
            'success': True,
            'id': data.user.pk,
            'score': data.score
        }
    except Score.DoesNotExist:
        r = {'success': False, 'message': 'user not found'}
    return JsonResponse(r)
