import logging
from pathlib import Path

from django.shortcuts import render, get_list_or_404

from ..models import Invoice, InvoiceItem

log = logging.getLogger(__name__)

template_path = Path("orderflow_app") / "invoices"


def invoices(request):
    invoices_list = Invoice.objects.all().order_by("-invoice_date")
    context = {
        "invoices": invoices_list,
    }
    return render(request, template_path/"invoices.html", context=context)


def invoice_items(request, invoice_id):
    invoice_items = get_list_or_404(InvoiceItem, invoice_id=invoice_id)
    context = {
        "invoiceitems": invoice_items
    }
    return render(request, template_path/"invoiceitems.html", context=context)
