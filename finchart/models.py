from django.db import models
import numpy # numpyを追加（10-2 ゼロ除算とは？）

# Create your models here.
# ---ここから追記(3-3 モデルの定義)---
class Company(models.Model):
    name = models.CharField("会社名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)
# ---ここまで---

# ---ここから追記(3-3 モデルの定義)---
class Fstatement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fiscal_year = models.DateField("決算日")
    bs_current_assets = models.IntegerField("流動資産（千円）", default=0)
    bs_fixed_assets = models.IntegerField("固定資産（千円）", default=0)
    bs_deferred_assets = models.IntegerField("繰延資産（千円）", default=0)
    bs_current_liabilities = models.IntegerField("流動負債（千円）", default=0)
    bs_fixed_liabilities = models.IntegerField("固定負債（千円）", default=0)
    bs_net_assets = models.IntegerField("純資産（千円）", default=0)
    pl_gross_sales = models.IntegerField("総売上（千円）", default=0)
    pl_gross_profit = models.IntegerField("売上総利益（千円）", default=0)
    pl_executive_salary = models.IntegerField("役員報酬（千円）", default=0)
    pl_employees_salary = models.IntegerField("給料手当（千円）", default=0)
    pl_employees_bonus = models.IntegerField("賞与（千円）", default=0)
    pl_legal_welfare_expenses = models.IntegerField("法定福利費（千円）", default=0)
    pl_welfare_expenses = models.IntegerField("福利厚生費（千円）", default=0)
    pl_educational_training_expenses = models.IntegerField("教育研修費（千円）", default=0)
    pl_tax_dues = models.IntegerField("租税公課（千円）", default=0)
    pl_entertainment_expenses = models.IntegerField("交際接待費（千円）", default=0)
    pl_contribution = models.IntegerField("寄付金（千円）", default=0)
    pl_commisission_fees = models.IntegerField("支払手数料（千円）", default=0)
    pl_add_expenses = models.IntegerField("広告宣伝費（千円）", default=0)
    pl_communication_expenses = models.IntegerField("通信費（千円）", default=0)
    pl_transportasion_expenses = models.IntegerField("旅費交通費（千円）", default=0)
    pl_repair_expenses = models.IntegerField("修繕費（千円）", default=0)
    pl_utilities_expenses = models.IntegerField("水道光熱費（千円）", default=0)
    pl_rent_expenses = models.IntegerField("賃借料・地代家賃（千円）", default=0)
    pl_lease_expenses = models.IntegerField("リース料（千円）", default=0)
    pl_packing_transportation_expenses = models.IntegerField("荷造運送費（千円）", default=0)
    pl_office_supplies_expenses = models.IntegerField("事務用品消耗品費（千円）", default=0)
    pl_newspapars_expenses = models.IntegerField("新聞図書費（千円）", default=0)
    pl_consulting_expenses = models.IntegerField("顧問料（千円）", default=0)
    pl_bussiness_consignment_expenses = models.IntegerField("業務委託費（千円）",default=0)
    pl_depreciation = models.IntegerField("その他償却費（千円）", default=0)
    pl_administrative_expenses = models.IntegerField("その他販売費及び一般管理費（千円）", default=0)
    pl_operating_profit = models.IntegerField("営業利益（千円）", default=0)
    pl_ordinary_income = models.IntegerField("経常利益（千円）", default=0)
    pl_income_before_tax = models.IntegerField("税引前当期純利益（千円）", default=0)
    pl_net_income = models.IntegerField("当期純利益（千円）", default=0)
    cf_operating = models.IntegerField("営業ＣＦ（千円）", default=0)
    cf_investment = models.IntegerField("投資ＣＦ（千円）", default=0)
    cf_finance = models.IntegerField("財務ＣＦ（千円）", default=0)

    def __str__(self):
        return str(self.company) + '決算日：【 ' + str(self.fiscal_year) + '】'
# ---ここまで---

    # ========以下をすべて追加（-3 モデル内に計算式を定義する）========

    # 総資産を計算
    def bs_total_assets(self):
        f = self.bs_current_assets + self.bs_fixed_assets + self.bs_deferred_assets
        return f

    # 総資産に対する流動資産の比率を計算（流動資産／総資産）
    def current_assets_rate(self):
        f = numpy.float64(self.bs_current_assets) / self.bs_total_assets() * 100
        return f

    # 総資産に対する固定資産の比率を計算（固定資産／総資産）
    def fixed_assets_rate(self):
        f = numpy.float64(self.bs_fixed_assets) / self.bs_total_assets() * 100
        return f

    # 総資産に対する繰延資産の比率を計算（繰延資産／総資産）
    def deferred_assets_rate(self):
        f = numpy.float64(self.bs_deferred_assets) / self.bs_total_assets() * 100
        return f

    # 総資産に対する流動負債の比率を計算（流動負債／総資産）
    def current_liabilities_rate(self):
        f = numpy.float64(self.bs_current_liabilities) / self.bs_total_assets() * 100
        return f

    # 総資産に対する固定負債の比率を計算（固定負債／総資産）
    def fixed_liabilities_rate(self):
        f = numpy.float64(self.bs_fixed_liabilities) / self.bs_total_assets() * 100
        return f

    # 総資産に対する純資産の比率を計算（純資産／総資産）
    def net_assets_rate(self):
        f = numpy.float64(self.bs_net_assets) / self.bs_total_assets() * 100
        return f

    # 総売上高合計に対する売上総利益の比率を計算（売上総利益／総売上）
    def gross_profit_rate(self):
        f = numpy.float64(self.pl_gross_profit) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する役員報酬の比率を計算（役員報酬／総売上）
    def executive_salary_rate(self):
        f = numpy.float64(self.pl_executive_salary) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する給料手当の比率を計算（給料手当／総売上）
    def employees_salary_rate(self):
        f = numpy.float64(self.pl_employees_salary) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する賞与の比率を計算（賞与／総売上）
    def employees_bonus_rate(self):
        f = numpy.float64(self.pl_employees_bonus) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する法定福利費の比率を計算（法定福利費／総売上）
    def legal_welfare_expenses_rate(self):
        f = numpy.float64(self.pl_legal_welfare_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する福利厚生費の比率を計算（福利厚生費／総売上）
    def welfare_expenses_rate(self):
        f = numpy.float64(self.pl_welfare_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する教育研修費の比率を計算（教育研修費／総売上）
    def educational_training_expenses_rate(self):
        f = numpy.float64(self.pl_educational_training_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する租税公課の比率を計算（租税公課／総売上）
    def tax_dues_rate(self):
        f = numpy.float64(self.pl_tax_dues) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する交際接待費の比率を計算（交際接待費／総売上）
    def entertainment_expenses_rate(self):
        f = numpy.float64(self.pl_entertainment_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する寄付金の比率を計算（寄付金／総売上）
    def contribution_rate(self):
        f = numpy.float64(self.pl_contribution) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する支払手数料の比率を計算（支払手数料／総売上）
    def commisission_fees_rate(self):
        f = numpy.float64(self.pl_commisission_fees) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する広告宣伝費の比率を計算（広告宣伝費／総売上）
    def add_expenses_rate(self):
        f = numpy.float64(self.pl_add_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する通信費の比率を計算（通信費／総売上）
    def communication_expenses_rate(self):
        f = numpy.float64(self.pl_communication_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する旅費交通費の比率を計算（旅費交通費／総売上）
    def transportasion_expenses_rate(self):
        f = numpy.float64(self.pl_transportasion_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する修繕費の比率を計算（修繕費／総売上）
    def repair_expenses_rate(self):
        f = numpy.float64(self.pl_repair_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する水道光熱費の比率を計算（水道光熱費／総売上）
    def utilities_expenses_rate(self):
        f = numpy.float64(self.pl_utilities_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する賃借料地代家賃の比率を計算（賃借料地代家賃／総売上）
    def rent_expenses_rate(self):
        f = numpy.float64(self.pl_rent_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対するリース料の比率を計算（リース料／総売上）
    def lease_expenses_rate(self):
        f = numpy.float64(self.pl_lease_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する荷造運送費の比率を計算（荷造運送費／総売上）
    def packing_transportation_expenses_rate(self):
        f = numpy.float64(self.pl_packing_transportation_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する事務用品消耗品費の比率を計算（事務用品消耗品費／総売上）
    def office_supplies_expenses_rate(self):
        f = numpy.float64(self.pl_office_supplies_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する新聞図書費の比率を計算（新聞図書費／総売上）
    def newspapars_expenses_rate(self):
        f = numpy.float64(self.pl_newspapars_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する顧問料の比率を計算（顧問料／総売上）
    def consulting_expenses_rate(self):
        f = numpy.float64(self.pl_consulting_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する業務委託費の比率を計算（業務委託費／総売上）
    def bussiness_consignment_expenses_rate(self):
        f = numpy.float64(self.pl_bussiness_consignment_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する償却費の比率を計算（償却費／総売上）
    def depreciation_rate(self):
        f = numpy.float64(self.pl_depreciation) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対するその他販売費及び一般管理費の比率を計算（その他販売費及び一般管理費／総売上）
    def administrative_expenses_rate(self):
        f = numpy.float64(self.pl_administrative_expenses) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する営業利益の比率を計算（営業利益／総売上）
    def operating_profit_rate(self):
        f = numpy.float64(self.pl_operating_profit) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する経常利益の比率を計算（経常利益／総売上）
    def ordinary_income_rate(self):
        f = numpy.float64(self.pl_ordinary_income) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する税引前当期純利益の比率を計算（税引前当期純利益／総売上）
    def income_before_tax_rate(self):
        f = numpy.float64(self.pl_income_before_tax) / self.pl_gross_sales * 100
        return f

    # 総売上高合計に対する当期純利益の比率を計算（当期純利益／総売上）
    def net_income_rate(self):
        f = numpy.float64(self.pl_net_income) / self.pl_gross_sales * 100
        return f

    # キャッシュフロー合計を計算
    def cf_total_amount(self):
        f = self.cf_operating + self.cf_investment + self.cf_finance
        return f

    # ========以下をすべて追加(9-3 財務指標の定義)========

    # 流動比率を計算
    def current_rate(self):
        if self.bs_current_liabilities > 0:
            f = numpy.float64(self.bs_current_assets) / self.bs_current_liabilities * 100
        else:
            f = '-'
        return f

    # ＲＯＥを計算
    def roe(self):
        f = numpy.float64(self.pl_operating_profit) / self.bs_net_assets * 100
        return f

    #　ＲＯＡを計算
    def roa(self):
        f = numpy.float64(self.pl_operating_profit) / self.bs_total_assets() * 100
        return f
