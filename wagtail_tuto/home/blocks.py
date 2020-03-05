from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class RowBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    datetime_google = blocks.CharBlock()
    datetime_reader = blocks.CharBlock()
    location_up = blocks.CharBlock()
    location_down = blocks.CharBlock()
    eventbrite = blocks.URLBlock()
    googlemap = blocks.URLBlock()
    description = blocks.RichTextBlock()