# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActivityLog(models.Model):
    log_name = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField()
    subject_id = models.IntegerField(blank=True, null=True)
    subject_type = models.CharField(max_length=191, blank=True, null=True)
    business_id = models.IntegerField(blank=True, null=True)
    causer_id = models.IntegerField(blank=True, null=True)
    causer_type = models.CharField(max_length=191, blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial283 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Barcodes(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    paper_width = models.FloatField(blank=True, null=True)
    paper_height = models.FloatField(blank=True, null=True)
    top_margin = models.FloatField(blank=True, null=True)
    left_margin = models.FloatField(blank=True, null=True)
    row_distance = models.FloatField(blank=True, null=True)
    col_distance = models.FloatField(blank=True, null=True)
    stickers_in_one_row = models.IntegerField(blank=True, null=True)
    is_default = models.SmallIntegerField()
    is_continuous = models.SmallIntegerField()
    stickers_in_one_sheet = models.IntegerField(blank=True, null=True)
    business = models.ForeignKey('Business', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcodes'


class Brands(models.Model):
    business = models.ForeignKey('Business', models.DO_NOTHING)
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    use_for_repair = models.SmallIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brands'


class Business(models.Model):
    name = models.CharField(max_length=191)
    currency = models.ForeignKey('Currencies', models.DO_NOTHING)
    start_date = models.DateField(blank=True, null=True)
    tax_number_1 = models.CharField(max_length=100, blank=True, null=True)
    tax_label_1 = models.CharField(max_length=10, blank=True, null=True)
    tax_number_2 = models.CharField(max_length=100, blank=True, null=True)
    tax_label_2 = models.CharField(max_length=10, blank=True, null=True)
    code_label_1 = models.CharField(max_length=191, blank=True, null=True)
    code_1 = models.CharField(max_length=191, blank=True, null=True)
    code_label_2 = models.CharField(max_length=191, blank=True, null=True)
    code_2 = models.CharField(max_length=191, blank=True, null=True)
    default_sales_tax = models.ForeignKey('TaxRates', models.DO_NOTHING, db_column='default_sales_tax', blank=True, null=True)
    default_profit_percent = models.FloatField()
    owner = models.ForeignKey('Users', models.DO_NOTHING)
    time_zone = models.CharField(max_length=191)
    fy_start_month = models.SmallIntegerField()
    accounting_method = models.CharField(max_length=4)
    default_sales_discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sell_price_tax = models.CharField(max_length=8)
    logo = models.CharField(max_length=191, blank=True, null=True)
    sku_prefix = models.CharField(max_length=191, blank=True, null=True)
    enable_product_expiry = models.SmallIntegerField()
    expiry_type = models.CharField(max_length=17)
    on_product_expiry = models.CharField(max_length=12)
    stop_selling_before = models.IntegerField()
    enable_tooltip = models.SmallIntegerField()
    purchase_in_diff_currency = models.SmallIntegerField()
    purchase_currency_id = models.BigIntegerField(blank=True, null=True)
    p_exchange_rate = models.DecimalField(max_digits=20, decimal_places=2)
    transaction_edit_days = models.BigIntegerField()
    stock_expiry_alert_days = models.BigIntegerField()
    keyboard_shortcuts = models.TextField(blank=True, null=True)
    pos_settings = models.TextField(blank=True, null=True)
    essentials_settings = models.TextField(blank=True, null=True)
    manufacturing_settings = models.TextField(blank=True, null=True)
    woocommerce_api_settings = models.TextField(blank=True, null=True)
    woocommerce_skipped_orders = models.TextField(blank=True, null=True)
    woocommerce_wh_oc_secret = models.CharField(max_length=191, blank=True, null=True)
    woocommerce_wh_ou_secret = models.CharField(max_length=191, blank=True, null=True)
    woocommerce_wh_od_secret = models.CharField(max_length=191, blank=True, null=True)
    woocommerce_wh_or_secret = models.CharField(max_length=191, blank=True, null=True)
    weighing_scale_setting = models.TextField()
    enable_brand = models.SmallIntegerField()
    enable_category = models.SmallIntegerField()
    enable_sub_category = models.SmallIntegerField()
    enable_price_tax = models.SmallIntegerField()
    enable_purchase_status = models.SmallIntegerField(blank=True, null=True)
    enable_lot_number = models.SmallIntegerField()
    default_unit = models.IntegerField(blank=True, null=True)
    enable_sub_units = models.SmallIntegerField()
    enable_racks = models.SmallIntegerField()
    enable_row = models.SmallIntegerField()
    enable_position = models.SmallIntegerField()
    enable_editing_product_from_purchase = models.SmallIntegerField()
    sales_cmsn_agnt = models.CharField(max_length=14, blank=True, null=True)
    item_addition_method = models.SmallIntegerField()
    enable_inline_tax = models.SmallIntegerField()
    currency_symbol_placement = models.CharField(max_length=6)
    enabled_modules = models.TextField(blank=True, null=True)
    date_format = models.CharField(max_length=191)
    time_format = models.CharField(max_length=2)
    ref_no_prefixes = models.TextField(blank=True, null=True)
    theme_color = models.CharField(max_length=20, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    crm_settings = models.TextField(blank=True, null=True)
    repair_settings = models.TextField(blank=True, null=True)
    enable_rp = models.SmallIntegerField()
    rp_name = models.CharField(max_length=191, blank=True, null=True)
    amount_for_unit_rp = models.DecimalField(max_digits=22, decimal_places=0)
    min_order_total_for_rp = models.DecimalField(max_digits=22, decimal_places=0)
    max_rp_per_order = models.IntegerField(blank=True, null=True)
    redeem_amount_per_unit_rp = models.DecimalField(max_digits=22, decimal_places=0)
    min_order_total_for_redeem = models.DecimalField(max_digits=22, decimal_places=0)
    min_redeem_point = models.IntegerField(blank=True, null=True)
    max_redeem_point = models.IntegerField(blank=True, null=True)
    rp_expiry_period = models.IntegerField(blank=True, null=True)
    rp_expiry_type = models.CharField(max_length=5)
    email_settings = models.TextField(blank=True, null=True)
    sms_settings = models.TextField(blank=True, null=True)
    custom_labels = models.TextField(blank=True, null=True)
    common_settings = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business'


class BusinessLocations(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    location_id = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=256)
    landmark = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=7)
    invoice_scheme = models.ForeignKey('InvoiceSchemes', models.DO_NOTHING)
    invoice_layout = models.ForeignKey('InvoiceLayouts', models.DO_NOTHING)
    sale_invoice_layout_id = models.IntegerField(blank=True, null=True)
    selling_price_group_id = models.IntegerField(blank=True, null=True)
    print_receipt_on_invoice = models.SmallIntegerField(blank=True, null=True)
    receipt_printer_type = models.CharField(max_length=7)
    printer_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=191, blank=True, null=True)
    alternate_number = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    website = models.CharField(max_length=191, blank=True, null=True)
    featured_products = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    default_payment_accounts = models.TextField(blank=True, null=True)
    custom_field1 = models.CharField(max_length=191, blank=True, null=True)
    custom_field2 = models.CharField(max_length=191, blank=True, null=True)
    custom_field3 = models.CharField(max_length=191, blank=True, null=True)
    custom_field4 = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business_locations'


class CashRegisterTransactions(models.Model):
    cash_register = models.ForeignKey('CashRegisters', models.DO_NOTHING)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    pay_method = models.CharField(max_length=191, blank=True, null=True)
    type = models.CharField(max_length=6)
    transaction_type = models.CharField(max_length=191, blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_register_transactions'


class CashRegisters(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    location_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=5)
    closed_at = models.DateTimeField(blank=True, null=True)
    closing_amount = models.DecimalField(max_digits=22, decimal_places=2)
    total_card_slips = models.IntegerField()
    total_cheques = models.IntegerField()
    denominations = models.TextField(blank=True, null=True)
    closing_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_registers'


class Categories(models.Model):
    name = models.CharField(max_length=191)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    short_code = models.CharField(max_length=191, blank=True, null=True)
    parent_id = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    woocommerce_cat_id = models.IntegerField(blank=True, null=True)
    category_type = models.CharField(max_length=191, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class CategoryCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_category'


class Contacts(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    type = models.CharField(max_length=191)
    supplier_business_name = models.CharField(max_length=191, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    prefix = models.CharField(max_length=191, blank=True, null=True)
    first_name = models.CharField(max_length=191, blank=True, null=True)
    middle_name = models.CharField(max_length=191, blank=True, null=True)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    contact_id = models.CharField(max_length=191, blank=True, null=True)
    contact_status = models.CharField(max_length=191)
    tax_number = models.CharField(max_length=191, blank=True, null=True)
    city = models.CharField(max_length=191, blank=True, null=True)
    state = models.CharField(max_length=191, blank=True, null=True)
    country = models.CharField(max_length=191, blank=True, null=True)
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    zip_code = models.CharField(max_length=191, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    mobile = models.CharField(max_length=191)
    landline = models.CharField(max_length=191, blank=True, null=True)
    alternate_number = models.CharField(max_length=191, blank=True, null=True)
    pay_term_number = models.IntegerField(blank=True, null=True)
    pay_term_type = models.CharField(max_length=6, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    converted_by = models.IntegerField(blank=True, null=True)
    converted_on = models.DateTimeField(blank=True, null=True)
    balance = models.DecimalField(max_digits=22, decimal_places=2)
    total_rp = models.IntegerField()
    total_rp_used = models.IntegerField()
    total_rp_expired = models.IntegerField()
    is_default = models.SmallIntegerField()
    shipping_address = models.TextField(blank=True, null=True)
    shipping_custom_field_details = models.TextField(blank=True, null=True)
    is_export = models.SmallIntegerField()
    export_custom_field_1 = models.CharField(max_length=191, blank=True, null=True)
    export_custom_field_2 = models.CharField(max_length=191, blank=True, null=True)
    export_custom_field_3 = models.CharField(max_length=191, blank=True, null=True)
    export_custom_field_4 = models.CharField(max_length=191, blank=True, null=True)
    export_custom_field_5 = models.CharField(max_length=191, blank=True, null=True)
    export_custom_field_6 = models.CharField(max_length=191, blank=True, null=True)
    position = models.CharField(max_length=191, blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    crm_source = models.CharField(max_length=191, blank=True, null=True)
    crm_life_stage = models.CharField(max_length=191, blank=True, null=True)
    custom_field1 = models.CharField(max_length=191, blank=True, null=True)
    custom_field2 = models.CharField(max_length=191, blank=True, null=True)
    custom_field3 = models.CharField(max_length=191, blank=True, null=True)
    custom_field4 = models.CharField(max_length=191, blank=True, null=True)
    custom_field5 = models.CharField(max_length=191, blank=True, null=True)
    custom_field6 = models.CharField(max_length=191, blank=True, null=True)
    custom_field7 = models.CharField(max_length=191, blank=True, null=True)
    custom_field8 = models.CharField(max_length=191, blank=True, null=True)
    custom_field9 = models.CharField(max_length=191, blank=True, null=True)
    custom_field10 = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class CrmScheduleUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    schedule = models.ForeignKey('CrmSchedules', models.DO_NOTHING)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_schedule_users'


class CrmSchedules(models.Model):
    id = models.BigAutoField(primary_key=True)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    contact_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=191)
    status = models.CharField(max_length=191, blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    schedule_type = models.CharField(max_length=7)
    allow_notification = models.SmallIntegerField()
    notify_via = models.TextField(blank=True, null=True)
    notify_before = models.IntegerField(blank=True, null=True)
    notify_type = models.CharField(max_length=6)
    created_by = models.IntegerField()
    is_recursive = models.SmallIntegerField()
    recursion_days = models.IntegerField(blank=True, null=True)
    followup_additional_info = models.TextField(blank=True, null=True)
    follow_up_by = models.CharField(max_length=191, blank=True, null=True)
    follow_up_by_value = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_schedules'


class Currencies(models.Model):
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    code = models.CharField(max_length=25)
    symbol = models.CharField(max_length=25)
    thousand_separator = models.CharField(max_length=10)
    decimal_separator = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currencies'


class CustomerGroups(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    amount = models.FloatField()
    price_calculation_type = models.CharField(max_length=191, blank=True, null=True)
    selling_price_group_id = models.IntegerField(blank=True, null=True)
    created_by = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_groups'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExpenseCategories(models.Model):
    name = models.CharField(max_length=191)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    code = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'expense_categories'


class GroupSubTaxes(models.Model):
    group_tax = models.ForeignKey('TaxRates', models.DO_NOTHING)
    tax = models.ForeignKey('TaxRates', models.DO_NOTHING)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_sub_taxes'


class InvoiceLayouts(models.Model):
    name = models.CharField(max_length=191)
    header_text = models.TextField(blank=True, null=True)
    invoice_no_prefix = models.CharField(max_length=191, blank=True, null=True)
    quotation_no_prefix = models.CharField(max_length=191, blank=True, null=True)
    invoice_heading = models.CharField(max_length=191, blank=True, null=True)
    sub_heading_line1 = models.CharField(max_length=191, blank=True, null=True)
    sub_heading_line2 = models.CharField(max_length=191, blank=True, null=True)
    sub_heading_line3 = models.CharField(max_length=191, blank=True, null=True)
    sub_heading_line4 = models.CharField(max_length=191, blank=True, null=True)
    sub_heading_line5 = models.CharField(max_length=191, blank=True, null=True)
    invoice_heading_not_paid = models.CharField(max_length=191, blank=True, null=True)
    invoice_heading_paid = models.CharField(max_length=191, blank=True, null=True)
    quotation_heading = models.CharField(max_length=191, blank=True, null=True)
    sub_total_label = models.CharField(max_length=191, blank=True, null=True)
    discount_label = models.CharField(max_length=191, blank=True, null=True)
    tax_label = models.CharField(max_length=191, blank=True, null=True)
    total_label = models.CharField(max_length=191, blank=True, null=True)
    round_off_label = models.CharField(max_length=191, blank=True, null=True)
    total_due_label = models.CharField(max_length=191, blank=True, null=True)
    paid_label = models.CharField(max_length=191, blank=True, null=True)
    show_client_id = models.SmallIntegerField()
    client_id_label = models.CharField(max_length=191, blank=True, null=True)
    client_tax_label = models.CharField(max_length=191, blank=True, null=True)
    date_label = models.CharField(max_length=191, blank=True, null=True)
    date_time_format = models.CharField(max_length=191, blank=True, null=True)
    show_time = models.SmallIntegerField()
    show_brand = models.SmallIntegerField()
    show_sku = models.SmallIntegerField()
    show_cat_code = models.SmallIntegerField()
    show_expiry = models.SmallIntegerField()
    show_lot = models.SmallIntegerField()
    show_image = models.SmallIntegerField()
    show_sale_description = models.SmallIntegerField()
    sales_person_label = models.CharField(max_length=191, blank=True, null=True)
    show_sales_person = models.SmallIntegerField()
    table_product_label = models.CharField(max_length=191, blank=True, null=True)
    table_qty_label = models.CharField(max_length=191, blank=True, null=True)
    table_unit_price_label = models.CharField(max_length=191, blank=True, null=True)
    table_subtotal_label = models.CharField(max_length=191, blank=True, null=True)
    cat_code_label = models.CharField(max_length=191, blank=True, null=True)
    logo = models.CharField(max_length=191, blank=True, null=True)
    show_logo = models.SmallIntegerField()
    show_business_name = models.SmallIntegerField()
    show_location_name = models.SmallIntegerField()
    show_landmark = models.SmallIntegerField()
    show_city = models.SmallIntegerField()
    show_state = models.SmallIntegerField()
    show_zip_code = models.SmallIntegerField()
    show_country = models.SmallIntegerField()
    show_mobile_number = models.SmallIntegerField()
    show_alternate_number = models.SmallIntegerField()
    show_email = models.SmallIntegerField()
    show_tax_1 = models.SmallIntegerField()
    show_tax_2 = models.SmallIntegerField()
    show_barcode = models.SmallIntegerField()
    show_payments = models.SmallIntegerField()
    show_customer = models.SmallIntegerField()
    customer_label = models.CharField(max_length=191, blank=True, null=True)
    commission_agent_label = models.CharField(max_length=191, blank=True, null=True)
    show_commission_agent = models.SmallIntegerField()
    show_reward_point = models.SmallIntegerField()
    highlight_color = models.CharField(max_length=10, blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)
    common_settings = models.TextField(blank=True, null=True)
    is_default = models.SmallIntegerField()
    business = models.ForeignKey(Business, models.DO_NOTHING)
    show_qr_code = models.SmallIntegerField()
    qr_code_fields = models.TextField(blank=True, null=True)
    design = models.CharField(max_length=190, blank=True, null=True)
    cn_heading = models.CharField(max_length=191, blank=True, null=True)
    cn_no_label = models.CharField(max_length=191, blank=True, null=True)
    cn_amount_label = models.CharField(max_length=191, blank=True, null=True)
    table_tax_headings = models.TextField(blank=True, null=True)
    show_previous_bal = models.SmallIntegerField()
    prev_bal_label = models.CharField(max_length=191, blank=True, null=True)
    change_return_label = models.CharField(max_length=191, blank=True, null=True)
    product_custom_fields = models.TextField(blank=True, null=True)
    contact_custom_fields = models.TextField(blank=True, null=True)
    location_custom_fields = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_layouts'


class InvoiceSchemes(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    scheme_type = models.CharField(max_length=5)
    prefix = models.CharField(max_length=191, blank=True, null=True)
    start_number = models.IntegerField(blank=True, null=True)
    invoice_count = models.IntegerField()
    total_digits = models.IntegerField(blank=True, null=True)
    is_default = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_schemes'


class Media(models.Model):
    business_id = models.IntegerField()
    file_name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.IntegerField(blank=True, null=True)
    model_type = models.CharField(max_length=191)
    woocommerce_media_id = models.IntegerField(blank=True, null=True)
    model_media_type = models.CharField(max_length=191, blank=True, null=True)
    model_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial290 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class MfgIngredientGroups(models.Model):
    name = models.CharField(max_length=191)
    business_id = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfg_ingredient_groups'


class MfgRecipeIngredients(models.Model):
    mfg_recipe = models.ForeignKey('MfgRecipes', models.DO_NOTHING)
    variation_id = models.IntegerField()
    mfg_ingredient_group_id = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=22, decimal_places=4)
    waste_percent = models.DecimalField(max_digits=22, decimal_places=4)
    sub_unit_id = models.IntegerField(blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfg_recipe_ingredients'


class MfgRecipes(models.Model):
    product_id = models.IntegerField()
    variation_id = models.IntegerField()
    instructions = models.TextField(blank=True, null=True)
    waste_percent = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients_cost = models.DecimalField(max_digits=22, decimal_places=4)
    extra_cost = models.DecimalField(max_digits=22, decimal_places=4)
    production_cost_type = models.CharField(max_length=191, blank=True, null=True)
    total_quantity = models.DecimalField(max_digits=22, decimal_places=4)
    final_price = models.DecimalField(max_digits=22, decimal_places=4)
    sub_unit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mfg_recipes'


class Migrations(models.Model):
    migration = models.CharField(max_length=191)
    batch = models.IntegerField()
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=191)
    model_id = models.BigIntegerField()
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=191)
    model_id = models.BigIntegerField()
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class NotificationTemplates(models.Model):
    business_id = models.IntegerField()
    template_for = models.CharField(max_length=191)
    email_body = models.TextField(blank=True, null=True)
    sms_body = models.TextField(blank=True, null=True)
    whatsapp_text = models.TextField(blank=True, null=True)
    subject = models.CharField(max_length=191, blank=True, null=True)
    cc = models.CharField(max_length=191, blank=True, null=True)
    bcc = models.CharField(max_length=191, blank=True, null=True)
    auto_send = models.SmallIntegerField()
    auto_send_sms = models.SmallIntegerField()
    auto_send_wa_notif = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_templates'


class Notifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    type = models.CharField(max_length=191)
    notifiable_type = models.CharField(max_length=191)
    notifiable_id = models.BigIntegerField()
    data = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField(blank=True, null=True)
    client_id = models.BigIntegerField()
    name = models.CharField(max_length=191, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.BigIntegerField()
    client_id = models.BigIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.SmallIntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.SmallIntegerField()
    password_client = models.SmallIntegerField()
    revoked = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.SmallIntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class Packages(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    location_count = models.IntegerField()
    user_count = models.IntegerField()
    product_count = models.IntegerField()
    bookings = models.SmallIntegerField()
    kitchen = models.SmallIntegerField()
    order_screen = models.SmallIntegerField()
    tables = models.SmallIntegerField()
    invoice_count = models.IntegerField()
    interval = models.CharField(max_length=6)
    interval_count = models.IntegerField()
    trial_days = models.IntegerField()
    price = models.DecimalField(max_digits=22, decimal_places=2)
    custom_permissions = models.TextField()
    created_by = models.IntegerField()
    sort_order = models.IntegerField()
    is_active = models.SmallIntegerField()
    is_private = models.SmallIntegerField()
    is_one_time = models.SmallIntegerField()
    enable_custom_link = models.SmallIntegerField()
    custom_link = models.CharField(max_length=191, blank=True, null=True)
    custom_link_text = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'packages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=191)
    token = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class Permissions(models.Model):
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PjtInvoiceLines(models.Model):
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING)
    task = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=22, decimal_places=4)
    tax_rate_id = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=22, decimal_places=4)
    total = models.DecimalField(max_digits=22, decimal_places=4)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial300 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pjt_invoice_lines'


class PjtProjects(models.Model):
    business_id = models.IntegerField()
    name = models.CharField(max_length=191)
    contact_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=11)
    lead_id = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_by = models.IntegerField()
    settings = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pjt_projects'


class Printers(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    connection_type = models.CharField(max_length=7)
    capability_profile = models.CharField(max_length=8)
    char_per_line = models.CharField(max_length=191, blank=True, null=True)
    ip_address = models.CharField(max_length=191, blank=True, null=True)
    port = models.CharField(max_length=191, blank=True, null=True)
    path = models.CharField(max_length=191, blank=True, null=True)
    created_by = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial300 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printers'


class ProductLocations(models.Model):
    product_id = models.IntegerField()
    location_id = models.IntegerField()
    trial303 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_locations'


class ProductProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    photo = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    compare_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    sold = models.IntegerField()
    date_created = models.DateTimeField()
    category = models.ForeignKey(CategoryCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductVariations(models.Model):
    variation_template_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=191)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    is_dummy = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial303 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variations'


class Products(models.Model):
    name = models.CharField(max_length=191)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    type = models.CharField(max_length=8, blank=True, null=True)
    unit = models.ForeignKey('Units', models.DO_NOTHING, blank=True, null=True)
    sub_unit_ids = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    sub_category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    tax = models.ForeignKey('TaxRates', models.DO_NOTHING, db_column='tax', blank=True, null=True)
    tax_type = models.CharField(max_length=9)
    enable_stock = models.SmallIntegerField()
    alert_quantity = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    sku = models.CharField(max_length=191)
    barcode_type = models.CharField(max_length=5, blank=True, null=True)
    expiry_period = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    expiry_period_type = models.CharField(max_length=6, blank=True, null=True)
    enable_sr_no = models.SmallIntegerField()
    weight = models.CharField(max_length=191, blank=True, null=True)
    product_custom_field1 = models.CharField(max_length=191, blank=True, null=True)
    product_custom_field2 = models.CharField(max_length=191, blank=True, null=True)
    product_custom_field3 = models.CharField(max_length=191, blank=True, null=True)
    product_custom_field4 = models.CharField(max_length=191, blank=True, null=True)
    image = models.CharField(max_length=191, blank=True, null=True)
    woocommerce_media_id = models.IntegerField(blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    woocommerce_product_id = models.IntegerField(blank=True, null=True)
    woocommerce_disable_sync = models.SmallIntegerField()
    warranty_id = models.IntegerField(blank=True, null=True)
    is_inactive = models.SmallIntegerField()
    repair_model = models.ForeignKey('RepairDeviceModels', models.DO_NOTHING, blank=True, null=True)
    not_for_selling = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial303 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class ProductsLocationsSerial(models.Model):
    prod_loc_serial_id = models.BigAutoField(primary_key=True)
    business_loc = models.ForeignKey(BusinessLocations, models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    serial = models.CharField(max_length=25)
    operacion_in = models.CharField(max_length=25)
    ref_in = models.CharField(max_length=25)
    operacion_out = models.CharField(max_length=25, blank=True, null=True)
    ref_out = models.CharField(max_length=25, blank=True, null=True)
    activo = models.SmallIntegerField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial306 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products_locations_serial'


class PurchaseLines(models.Model):
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    variation = models.ForeignKey('Variations', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=22, decimal_places=0)
    pp_without_discount = models.DecimalField(max_digits=22, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=22, decimal_places=2)
    purchase_price_inc_tax = models.DecimalField(max_digits=22, decimal_places=2)
    item_tax = models.DecimalField(max_digits=22, decimal_places=2)
    tax = models.ForeignKey('TaxRates', models.DO_NOTHING, blank=True, null=True)
    purchase_order_line_id = models.IntegerField(blank=True, null=True)
    quantity_sold = models.DecimalField(max_digits=22, decimal_places=0)
    quantity_adjusted = models.DecimalField(max_digits=22, decimal_places=0)
    quantity_returned = models.DecimalField(max_digits=22, decimal_places=0)
    po_quantity_purchased = models.DecimalField(max_digits=22, decimal_places=0)
    mfg_quantity_used = models.DecimalField(max_digits=22, decimal_places=0)
    mfg_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    lot_number = models.CharField(max_length=191, blank=True, null=True)
    sub_unit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial309 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_lines'


class ReferenceCounts(models.Model):
    ref_type = models.CharField(max_length=191)
    ref_count = models.IntegerField()
    business_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference_counts'


class RepairDeviceModels(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    repair_checklist = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_device_models'


class RepairJobSheets(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    location_id = models.BigIntegerField(blank=True, null=True)
    contact = models.ForeignKey(Contacts, models.DO_NOTHING)
    job_sheet_no = models.CharField(max_length=191)
    service_type = models.CharField(max_length=8)
    pick_up_on_site_addr = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True)
    device = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    device_model = models.ForeignKey(RepairDeviceModels, models.DO_NOTHING, blank=True, null=True)
    checklist = models.TextField(blank=True, null=True)
    security_pwd = models.CharField(max_length=191, blank=True, null=True)
    security_pattern = models.CharField(max_length=191, blank=True, null=True)
    serial_no = models.CharField(max_length=191)
    status_id = models.IntegerField()
    delivery_date = models.DateTimeField(blank=True, null=True)
    product_configuration = models.TextField(blank=True, null=True)
    defects = models.TextField(blank=True, null=True)
    product_condition = models.TextField(blank=True, null=True)
    service_staff = models.ForeignKey('Users', models.DO_NOTHING, db_column='service_staff', blank=True, null=True)
    comment_by_ss = models.TextField(blank=True, null=True)
    estimated_cost = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    parts = models.TextField(blank=True, null=True)
    custom_field_1 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_2 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_3 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_4 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_5 = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_job_sheets'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    name = models.CharField(max_length=191)
    guard_name = models.CharField(max_length=191)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    is_default = models.SmallIntegerField()
    is_service_staff = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial293 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SellingPriceGroups(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    is_active = models.SmallIntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'selling_price_groups'


class SocialAuthAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    id = models.BigAutoField(primary_key=True)
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    id = models.BigAutoField(primary_key=True)
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class Subscriptions(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    package_id = models.BigIntegerField()
    start_date = models.DateField(blank=True, null=True)
    trial_end_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    package_price = models.DecimalField(max_digits=22, decimal_places=2)
    package_details = models.TextField()
    created_id = models.BigIntegerField()
    paid_via = models.CharField(max_length=191, blank=True, null=True)
    payment_transaction_id = models.CharField(max_length=191, blank=True, null=True)
    status = models.CharField(max_length=8)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class System(models.Model):
    key = models.CharField(max_length=191)
    value = models.TextField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system'


class TaxRates(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    name = models.CharField(max_length=191)
    amount = models.FloatField()
    is_tax_group = models.SmallIntegerField()
    for_tax_group = models.SmallIntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    woocommerce_tax_rate_id = models.IntegerField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_rates'


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class TransactionPayments(models.Model):
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING, blank=True, null=True)
    business_id = models.IntegerField(blank=True, null=True)
    is_return = models.SmallIntegerField()
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    method = models.CharField(max_length=191, blank=True, null=True)
    transaction_no = models.CharField(max_length=191, blank=True, null=True)
    card_transaction_number = models.CharField(max_length=191, blank=True, null=True)
    card_number = models.CharField(max_length=191, blank=True, null=True)
    card_type = models.CharField(max_length=191, blank=True, null=True)
    card_holder_name = models.CharField(max_length=191, blank=True, null=True)
    card_month = models.CharField(max_length=191, blank=True, null=True)
    card_year = models.CharField(max_length=191, blank=True, null=True)
    card_security = models.CharField(max_length=5, blank=True, null=True)
    cheque_number = models.CharField(max_length=191, blank=True, null=True)
    bank_account_number = models.CharField(max_length=191, blank=True, null=True)
    paid_on = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    paid_through_link = models.SmallIntegerField()
    gateway = models.CharField(max_length=191, blank=True, null=True)
    is_advance = models.SmallIntegerField()
    payment_for = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    note = models.CharField(max_length=191, blank=True, null=True)
    document = models.CharField(max_length=191, blank=True, null=True)
    payment_ref_no = models.CharField(max_length=191, blank=True, null=True)
    account_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_payments'


class TransactionSellLines(models.Model):
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    variation = models.ForeignKey('Variations', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=22, decimal_places=0)
    mfg_waste_percent = models.DecimalField(max_digits=22, decimal_places=2)
    quantity_returned = models.DecimalField(max_digits=20, decimal_places=0)
    unit_price_before_discount = models.DecimalField(max_digits=22, decimal_places=2)
    unit_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    line_discount_type = models.CharField(max_length=10, blank=True, null=True)
    line_discount_amount = models.DecimalField(max_digits=22, decimal_places=2)
    unit_price_inc_tax = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    item_tax = models.DecimalField(max_digits=22, decimal_places=2)
    tax = models.ForeignKey(TaxRates, models.DO_NOTHING, blank=True, null=True)
    discount_id = models.IntegerField(blank=True, null=True)
    lot_no_line_id = models.IntegerField(blank=True, null=True)
    sell_line_note = models.TextField(blank=True, null=True)
    woocommerce_line_items_id = models.IntegerField(blank=True, null=True)
    so_line_id = models.IntegerField(blank=True, null=True)
    so_quantity_invoiced = models.DecimalField(max_digits=22, decimal_places=0)
    res_service_staff_id = models.IntegerField(blank=True, null=True)
    res_line_order_status = models.CharField(max_length=191, blank=True, null=True)
    parent_sell_line_id = models.IntegerField(blank=True, null=True)
    children_type = models.CharField(max_length=191)
    sub_unit_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial313 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_sell_lines'


class TransactionSellLinesPurchaseLines(models.Model):
    sell_line_id = models.BigIntegerField(blank=True, null=True)
    stock_adjustment_line_id = models.BigIntegerField(blank=True, null=True)
    purchase_line_id = models.BigIntegerField()
    quantity = models.DecimalField(max_digits=22, decimal_places=0)
    qty_returned = models.DecimalField(max_digits=22, decimal_places=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial316 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_sell_lines_purchase_lines'


class Transactions(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    location = models.ForeignKey(BusinessLocations, models.DO_NOTHING, blank=True, null=True)
    res_table_id = models.BigIntegerField(blank=True, null=True)
    res_waiter_id = models.BigIntegerField(blank=True, null=True)
    res_order_status = models.CharField(max_length=8, blank=True, null=True)
    type = models.CharField(max_length=191, blank=True, null=True)
    sub_type = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=191)
    sub_status = models.CharField(max_length=191, blank=True, null=True)
    is_quotation = models.SmallIntegerField()
    payment_status = models.CharField(max_length=7, blank=True, null=True)
    adjustment_type = models.CharField(max_length=8, blank=True, null=True)
    contact = models.ForeignKey(Contacts, models.DO_NOTHING, blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    invoice_no = models.CharField(max_length=191, blank=True, null=True)
    ref_no = models.CharField(max_length=191, blank=True, null=True)
    source = models.CharField(max_length=191, blank=True, null=True)
    subscription_no = models.CharField(max_length=191, blank=True, null=True)
    subscription_repeat_on = models.CharField(max_length=191, blank=True, null=True)
    transaction_date = models.DateTimeField()
    total_before_tax = models.DecimalField(max_digits=22, decimal_places=2)
    tax = models.ForeignKey(TaxRates, models.DO_NOTHING, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=22, decimal_places=4)
    discount_type = models.CharField(max_length=10, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    rp_redeemed = models.IntegerField()
    rp_redeemed_amount = models.DecimalField(max_digits=22, decimal_places=4)
    shipping_details = models.CharField(max_length=191, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    shipping_status = models.CharField(max_length=191, blank=True, null=True)
    delivered_to = models.CharField(max_length=191, blank=True, null=True)
    shipping_charges = models.DecimalField(max_digits=22, decimal_places=2)
    shipping_custom_field_1 = models.CharField(max_length=191, blank=True, null=True)
    shipping_custom_field_2 = models.CharField(max_length=191, blank=True, null=True)
    shipping_custom_field_3 = models.CharField(max_length=191, blank=True, null=True)
    shipping_custom_field_4 = models.CharField(max_length=191, blank=True, null=True)
    shipping_custom_field_5 = models.CharField(max_length=191, blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    staff_note = models.TextField(blank=True, null=True)
    is_export = models.SmallIntegerField()
    export_custom_fields_info = models.TextField(blank=True, null=True)
    round_off_amount = models.DecimalField(max_digits=22, decimal_places=4)
    additional_expense_key_1 = models.CharField(max_length=191, blank=True, null=True)
    additional_expense_value_1 = models.DecimalField(max_digits=22, decimal_places=4)
    additional_expense_key_2 = models.CharField(max_length=191, blank=True, null=True)
    additional_expense_value_2 = models.DecimalField(max_digits=22, decimal_places=4)
    additional_expense_key_3 = models.CharField(max_length=191, blank=True, null=True)
    additional_expense_value_3 = models.DecimalField(max_digits=22, decimal_places=4)
    additional_expense_key_4 = models.CharField(max_length=191, blank=True, null=True)
    additional_expense_value_4 = models.DecimalField(max_digits=22, decimal_places=4)
    final_total = models.DecimalField(max_digits=22, decimal_places=4)
    expense_category = models.ForeignKey(ExpenseCategories, models.DO_NOTHING, blank=True, null=True)
    expense_for = models.ForeignKey('Users', models.DO_NOTHING, db_column='expense_for', blank=True, null=True)
    commission_agent = models.IntegerField(blank=True, null=True)
    document = models.CharField(max_length=191, blank=True, null=True)
    is_direct_sale = models.SmallIntegerField()
    is_suspend = models.SmallIntegerField()
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=3)
    total_amount_recovered = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    transfer_parent_id = models.IntegerField(blank=True, null=True)
    return_parent_id = models.IntegerField(blank=True, null=True)
    opening_stock_product_id = models.IntegerField(blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    crm_is_order_request = models.SmallIntegerField()
    essentials_duration = models.DecimalField(max_digits=8, decimal_places=2)
    essentials_duration_unit = models.CharField(max_length=20, blank=True, null=True)
    essentials_amount_per_unit_duration = models.DecimalField(max_digits=22, decimal_places=4)
    essentials_allowances = models.TextField(blank=True, null=True)
    essentials_deductions = models.TextField(blank=True, null=True)
    mfg_parent_production_purchase_id = models.IntegerField(blank=True, null=True)
    mfg_wasted_units = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    mfg_production_cost = models.DecimalField(max_digits=22, decimal_places=4)
    mfg_production_cost_type = models.CharField(max_length=191, blank=True, null=True)
    mfg_is_final = models.SmallIntegerField()
    repair_completed_on = models.DateTimeField(blank=True, null=True)
    repair_warranty_id = models.IntegerField(blank=True, null=True)
    repair_brand_id = models.IntegerField(blank=True, null=True)
    repair_status_id = models.IntegerField(blank=True, null=True)
    repair_model_id = models.IntegerField(blank=True, null=True)
    repair_job_sheet = models.ForeignKey(RepairJobSheets, models.DO_NOTHING, blank=True, null=True)
    repair_defects = models.TextField(blank=True, null=True)
    repair_serial_no = models.CharField(max_length=191, blank=True, null=True)
    repair_checklist = models.TextField(blank=True, null=True)
    repair_security_pwd = models.CharField(max_length=191, blank=True, null=True)
    repair_security_pattern = models.CharField(max_length=191, blank=True, null=True)
    repair_due_date = models.DateTimeField(blank=True, null=True)
    repair_device_id = models.IntegerField(blank=True, null=True)
    repair_updates_notif = models.SmallIntegerField()
    woocommerce_order_id = models.IntegerField(blank=True, null=True)
    prefer_payment_method = models.CharField(max_length=191, blank=True, null=True)
    prefer_payment_account = models.IntegerField(blank=True, null=True)
    sales_order_ids = models.TextField(blank=True, null=True)
    purchase_order_ids = models.TextField(blank=True, null=True)
    custom_field_1 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_2 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_3 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_4 = models.CharField(max_length=191, blank=True, null=True)
    import_batch = models.IntegerField(blank=True, null=True)
    import_time = models.DateTimeField(blank=True, null=True)
    types_of_service_id = models.IntegerField(blank=True, null=True)
    packing_charge = models.DecimalField(max_digits=22, decimal_places=4, blank=True, null=True)
    packing_charge_type = models.CharField(max_length=7, blank=True, null=True)
    service_custom_field_1 = models.TextField(blank=True, null=True)
    service_custom_field_2 = models.TextField(blank=True, null=True)
    service_custom_field_3 = models.TextField(blank=True, null=True)
    service_custom_field_4 = models.TextField(blank=True, null=True)
    service_custom_field_5 = models.TextField(blank=True, null=True)
    service_custom_field_6 = models.TextField(blank=True, null=True)
    is_created_from_api = models.SmallIntegerField()
    rp_earned = models.IntegerField()
    order_addresses = models.TextField(blank=True, null=True)
    is_recurring = models.SmallIntegerField()
    recur_interval = models.FloatField(blank=True, null=True)
    recur_interval_type = models.CharField(max_length=6, blank=True, null=True)
    recur_repetitions = models.IntegerField(blank=True, null=True)
    recur_stopped_on = models.DateTimeField(blank=True, null=True)
    recur_parent_id = models.IntegerField(blank=True, null=True)
    invoice_token = models.CharField(max_length=191, blank=True, null=True)
    pay_term_number = models.IntegerField(blank=True, null=True)
    pay_term_type = models.CharField(max_length=6, blank=True, null=True)
    pjt_project = models.ForeignKey(PjtProjects, models.DO_NOTHING, blank=True, null=True)
    pjt_title = models.CharField(max_length=191, blank=True, null=True)
    selling_price_group_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial296 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Units(models.Model):
    business = models.ForeignKey(Business, models.DO_NOTHING)
    actual_name = models.CharField(max_length=191)
    short_name = models.CharField(max_length=191)
    allow_decimal = models.SmallIntegerField()
    base_unit_id = models.IntegerField(blank=True, null=True)
    base_unit_multiplier = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    created_by = models.ForeignKey('Users', models.DO_NOTHING, db_column='created_by')
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial303 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'units'


class UserUseraccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'user_useraccount'


class UserUseraccountGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    useraccount = models.ForeignKey(UserUseraccount, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_useraccount_groups'
        unique_together = (('useraccount', 'group'),)


class UserUseraccountUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    useraccount = models.ForeignKey(UserUseraccount, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_useraccount_user_permissions'
        unique_together = (('useraccount', 'permission'),)


class Users(models.Model):
    user_type = models.CharField(max_length=191)
    surname = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=191)
    last_name = models.CharField(max_length=191, blank=True, null=True)
    username = models.CharField(unique=True, max_length=191, blank=True, null=True)
    email = models.CharField(max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    language = models.CharField(max_length=7)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    business = models.ForeignKey(Business, models.DO_NOTHING, blank=True, null=True)
    essentials_department_id = models.IntegerField(blank=True, null=True)
    essentials_designation_id = models.IntegerField(blank=True, null=True)
    max_sales_discount_percent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    allow_login = models.SmallIntegerField()
    status = models.CharField(max_length=10)
    crm_contact = models.ForeignKey(Contacts, models.DO_NOTHING, blank=True, null=True)
    is_cmmsn_agnt = models.SmallIntegerField()
    cmmsn_percent = models.DecimalField(max_digits=4, decimal_places=2)
    selected_contacts = models.SmallIntegerField()
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=191, blank=True, null=True)
    marital_status = models.CharField(max_length=9, blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    alt_number = models.CharField(max_length=191, blank=True, null=True)
    family_number = models.CharField(max_length=191, blank=True, null=True)
    fb_link = models.CharField(max_length=191, blank=True, null=True)
    twitter_link = models.CharField(max_length=191, blank=True, null=True)
    social_media_1 = models.CharField(max_length=191, blank=True, null=True)
    social_media_2 = models.CharField(max_length=191, blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    current_address = models.TextField(blank=True, null=True)
    guardian_name = models.CharField(max_length=191, blank=True, null=True)
    custom_field_1 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_2 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_3 = models.CharField(max_length=191, blank=True, null=True)
    custom_field_4 = models.CharField(max_length=191, blank=True, null=True)
    bank_details = models.TextField(blank=True, null=True)
    id_proof_name = models.CharField(max_length=191, blank=True, null=True)
    id_proof_number = models.CharField(max_length=191, blank=True, null=True)
    crm_department = models.CharField(max_length=191, blank=True, null=True)
    crm_designation = models.CharField(max_length=191, blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial287 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VariationGroupPrices(models.Model):
    variation = models.ForeignKey('Variations', models.DO_NOTHING)
    price_group = models.ForeignKey(SellingPriceGroups, models.DO_NOTHING)
    price_inc_tax = models.DecimalField(max_digits=22, decimal_places=2)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial316 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation_group_prices'


class VariationLocationDetails(models.Model):
    product_id = models.BigIntegerField()
    product_variation_id = models.BigIntegerField()
    variation = models.ForeignKey('Variations', models.DO_NOTHING)
    location = models.ForeignKey(BusinessLocations, models.DO_NOTHING)
    qty_available = models.DecimalField(max_digits=22, decimal_places=0)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial316 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation_location_details'


class VariationTemplates(models.Model):
    name = models.CharField(max_length=191)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    woocommerce_attr_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    trial319 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variation_templates'


class Variations(models.Model):
    name = models.CharField(max_length=191)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    sub_sku = models.CharField(max_length=191, blank=True, null=True)
    product_variation = models.ForeignKey(ProductVariations, models.DO_NOTHING)
    woocommerce_variation_id = models.IntegerField(blank=True, null=True)
    variation_value_id = models.IntegerField(blank=True, null=True)
    default_purchase_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    dpp_inc_tax = models.DecimalField(max_digits=22, decimal_places=2)
    profit_percent = models.DecimalField(max_digits=22, decimal_places=2)
    default_sell_price = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    sell_price_inc_tax = models.DecimalField(max_digits=22, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    combo_variations = models.TextField(blank=True, null=True)
    trial309 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'variations'
