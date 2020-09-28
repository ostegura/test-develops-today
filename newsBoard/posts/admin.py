from django.contrib import admin

from .models import Post, Comment

# Register your models here.

# provided user to see post comments in django admin


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    search_fields = ["title", "author"]
    list_filter = ["title", "author"]
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author",)
    search_fields = ["author"]
    list_filter = ["author", "creation_date"]
    list_per_page = 50
