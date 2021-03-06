# Generated by Django 3.0.5 on 2020-04-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finchart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fstatement',
            name='pl_add_expenses',
            field=models.IntegerField(default=0, verbose_name='広告宣伝費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_administrative_expenses',
            field=models.IntegerField(default=0, verbose_name='その他販売費及び一般管理費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_bussiness_consignment_expenses',
            field=models.IntegerField(default=0, verbose_name='業務委託費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_commisission_fees',
            field=models.IntegerField(default=0, verbose_name='支払手数料（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_communication_expenses',
            field=models.IntegerField(default=0, verbose_name='通信費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_consulting_expenses',
            field=models.IntegerField(default=0, verbose_name='顧問料（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_contribution',
            field=models.IntegerField(default=0, verbose_name='寄付金（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_depreciation',
            field=models.IntegerField(default=0, verbose_name='その他償却費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_educational_training_expenses',
            field=models.IntegerField(default=0, verbose_name='教育研修費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_employees_bonus',
            field=models.IntegerField(default=0, verbose_name='賞与（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_employees_salary',
            field=models.IntegerField(default=0, verbose_name='給料手当（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_entertainment_expenses',
            field=models.IntegerField(default=0, verbose_name='交際接待費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_executive_salary',
            field=models.IntegerField(default=0, verbose_name='役員報酬（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_lease_expenses',
            field=models.IntegerField(default=0, verbose_name='リース料（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_legal_welfare_expenses',
            field=models.IntegerField(default=0, verbose_name='法定福利費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_newspapars_expenses',
            field=models.IntegerField(default=0, verbose_name='新聞図書費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_office_supplies_expenses',
            field=models.IntegerField(default=0, verbose_name='事務用品消耗品費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_packing_transportation_expenses',
            field=models.IntegerField(default=0, verbose_name='荷造運送費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_rent_expenses',
            field=models.IntegerField(default=0, verbose_name='賃借料・地代家賃（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_repair_expenses',
            field=models.IntegerField(default=0, verbose_name='修繕費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_tax_dues',
            field=models.IntegerField(default=0, verbose_name='租税公課（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_transportasion_expenses',
            field=models.IntegerField(default=0, verbose_name='旅費交通費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_utilities_expenses',
            field=models.IntegerField(default=0, verbose_name='水道光熱費（千円）'),
        ),
        migrations.AddField(
            model_name='fstatement',
            name='pl_welfare_expenses',
            field=models.IntegerField(default=0, verbose_name='福利厚生費（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_current_assets',
            field=models.IntegerField(default=0, verbose_name='流動資産（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_current_liabilities',
            field=models.IntegerField(default=0, verbose_name='流動負債（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_deferred_assets',
            field=models.IntegerField(default=0, verbose_name='繰延資産（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_fixed_assets',
            field=models.IntegerField(default=0, verbose_name='固定資産（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_fixed_liabilities',
            field=models.IntegerField(default=0, verbose_name='固定負債（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='bs_net_assets',
            field=models.IntegerField(default=0, verbose_name='純資産（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='cf_finance',
            field=models.IntegerField(default=0, verbose_name='財務ＣＦ（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='cf_investment',
            field=models.IntegerField(default=0, verbose_name='投資ＣＦ（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='cf_operating',
            field=models.IntegerField(default=0, verbose_name='営業ＣＦ（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_gross_profit',
            field=models.IntegerField(default=0, verbose_name='売上総利益（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_gross_sales',
            field=models.IntegerField(default=0, verbose_name='総売上（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_income_before_tax',
            field=models.IntegerField(default=0, verbose_name='税引前当期純利益（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_net_income',
            field=models.IntegerField(default=0, verbose_name='当期純利益（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_operating_profit',
            field=models.IntegerField(default=0, verbose_name='営業利益（千円）'),
        ),
        migrations.AlterField(
            model_name='fstatement',
            name='pl_ordinary_income',
            field=models.IntegerField(default=0, verbose_name='経常利益（千円）'),
        ),
    ]
