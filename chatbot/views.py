
import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import ChatSession, Message
from .services import generate_response


@login_required
def home(request):

    chats = ChatSession.objects.filter(
        user=request.user
    ).order_by('-updated_at')

    return render(request, 'chatbot/home.html', {
        'chats': chats
    })


@login_required
@require_POST
def create_chat(request):

    chat = ChatSession.objects.create(
        user=request.user,
        title="New Chat"
    )

    return JsonResponse({
        'chat_id': chat.id,
        'title': chat.title
    })


@login_required
@require_POST
def chat(request):

    try:

        data = json.loads(request.body)

        user_message = data.get('message', '').strip()
        chat_id = data.get('chat_id')

        if not user_message:
            return JsonResponse({
                'error': 'Please enter a message.'
            }, status=400)

        # Get existing chat or create a new one

        if chat_id:

            conversation = get_object_or_404(
                ChatSession,
                id=chat_id,
                user=request.user
            )

        else:

            conversation = ChatSession.objects.create(
                user=request.user,
                title="New Chat"
            )

        # Save user message

        Message.objects.create(
            chat=conversation,
            role='user',
            content=user_message
        )

        # Generate title from first message

        if conversation.title == "New Chat":

            conversation.title = user_message[:50]

            conversation.save()

        # Retrieve recent conversation history

        recent_messages = list(
            conversation.messages.order_by('-created_at')[:12]
        )

        recent_messages.reverse()

        conversation_history = [
            {
                'role': msg.role,
                'content': msg.content
            }
            for msg in recent_messages
        ]

        # Get AI response

        ai_response = generate_response(conversation_history)

        if ai_response.startswith("Error:"):

            return JsonResponse({
                'error': ai_response
            }, status=503)

        # Save AI response

        Message.objects.create(
            chat=conversation,
            role='assistant',
            content=ai_response
        )

        conversation.save()

        return JsonResponse({
            'response': ai_response,
            'chat_id': conversation.id,
            'title': conversation.title
        })

    except json.JSONDecodeError:

        return JsonResponse({
            'error': 'Invalid request data.'
        }, status=400)


@login_required
def get_messages(request, chat_id):

    conversation = get_object_or_404(
        ChatSession,
        id=chat_id,
        user=request.user
    )

    messages = conversation.messages.all()

    message_data = [
        {
            'role': msg.role,
            'content': msg.content,
            'created_at': msg.created_at.strftime(
                '%Y-%m-%d %H:%M'
            )
        }
        for msg in messages
    ]

    return JsonResponse({
        'chat_id': conversation.id,
        'title': conversation.title,
        'messages': message_data
    })


@login_required
@require_POST
def delete_chat(request, chat_id):

    conversation = get_object_or_404(
        ChatSession,
        id=chat_id,
        user=request.user
    )

    conversation.delete()

    return JsonResponse({
        'success': True
    })
