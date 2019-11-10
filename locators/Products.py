from .locators_types import css

class Products:

    add_new_btn = (css,'.pull-right .btn-primary')

    form = (css, '#form-product')

    general = (css, 'a[href="#tab-general"]')
    name = (css, '#input-name1')
    description = (css, '.note-editing-area p')
    meta_tag = (css, '#input-meta-title1')
    product_tag = (css, '#input-tag1')

    data = (css, 'a[href="#tab-data"]')
    model = (css, '#input-model')
    tax_class = (css, '#input-tax-class')

    pick_a_product = (css, '[name="selected[]"]')

    save = (css, '.pull-right .btn-primary')
    edit_product = (css, 'a[data-original-title="Edit"]')
    delete_product = (css, '.pull-right .btn-danger')

    success_message = (css, '.alert-success')
