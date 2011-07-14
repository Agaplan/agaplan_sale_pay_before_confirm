from osv import osv, fields
from tools.translate import _

class aga_adv_sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
        'pay_before_confirm': fields.boolean('Pay before Confirm', help="When checked this order cannot be confirm until an advance invoice has been created AND paid."),
    }

    def allow_confirm(self, cr, uid, ids, context=None):
        missing_invoice = []
        missing_payment = []
        for order in self.browse(cr, uid, ids, context):
            # We don't care about those without pay_before_confirm
            if not order.pay_before_confirm:
                continue

            # Check if there is an advance invoice linked
            if not order.invoice_ids:
                missing_invoice.append( order.name )

            # Check all invoices linked to be paid
            inv_paid = reduce( lambda a,b: a and b.state=='paid', order.invoice_ids, True )
            if not inv_paid:
                missing_payment.append( order.name )

            if missing_invoice:
                raise osv.except_osv(
                        _("Missing Advance Invoice"),
                        _("You have not created advanced invoices for following orders:\n%s") %
                        ("\n".join(missing_invoice))
                        )

            if missing_payment:
                raise osv.except_osv(
                        _("Unpaid Advance Invoice"),
                        _("There are still unpaid advance invoices for following orders:\n%s") % 
                        ("\n".join(missing_payment))
                        )

        return True
aga_adv_sale_order()

# vim:et:sts=4
