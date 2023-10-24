from django.contrib.auth.decorators import login_required
from django.db.models import Max, Q
from django.shortcuts import render, get_object_or_404, redirect

from message.forms import ConversationMessageForm
from message.models import Item, Conversation


# Create your views here.
@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.customuser.id])

    if conversations:
        return redirect('message:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user.customuser)
            conversation.members.add(item.id_user)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user.customuser
            conversation_message.save()

            return inbox(request)
    else:
        form = ConversationMessageForm()

    return render(request, 'message/new_conversation.html', {
        'form': form
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.customuser.id])

    return render(request, 'message/inbox.html', {
        'conversations': conversations
    })


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.customuser.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user.customuser
            conversation_message.save()

            conversation.save()

            return redirect('message:detail', pk=pk)
        else:
            form = ConversationMessageForm()

        return render(request, 'message/detail.html', {
            'conversation': conversation,
            'form': form,
        })

    form = ConversationMessageForm()

    return render(request, 'message/detail.html', {
        'conversation': conversation,
        'form': form,
    })
