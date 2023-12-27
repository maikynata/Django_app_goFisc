import csv
from django.core.management.base import BaseCommand
from app.models import RegC170

class Command(BaseCommand):
    help = 'Import data from a text file to the RegC170 model'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='C:\\Users\\Avell\\Projects\\c170-sample.txt')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter='|')

            # Skip the header row
            next(reader)

            for row in reader:
                try:
                    reg_c170 = RegC170(
                        ID=int(row[2]),
                        ID_PAI=int(row[3]),
                        LINHA=int(row[4]),
                        HASH=int(row[5]),
                        REG=row[6],
                        NUM_ITEM=row[7],
                        COD_ITEM=row[8],
                        DESCR_COMPL=row[9],
                        QTD=float(row[10]),
                        UNID=row[11],
                        VL_ITEM=float(row[12]),
                        VL_DESC=float(row[13]),
                        IND_MOV=row[14],
                        CST_ICMS=row[15],
                        CFOP=row[16],
                        COD_NAT=row[17],
                        VL_BC_ICMS=float(row[18]),
                        ALIQ_ICMS=float(row[19]),
                        VL_ICMS=float(row[20]),
                        VL_BC_ICMS_ST=float(row[21]),
                        ALIQ_ST=float(row[22]),
                        VL_ICMS_ST=float(row[23]),
                        IND_APUR=row[24],
                        CST_IPI=row[25],
                        COD_ENQ=row[26],
                        VL_BC_IPI=float(row[27]),
                        ALIQ_IPI=float(row[28]),
                        VL_IPI=float(row[29]),
                        CST_PIS=row[30],
                        VL_BC_PIS=float(row[31]),
                        ALIQ_PIS_PERC=float(row[32]),
                        QUANT_BC_PIS=float(row[33]),
                        ALIQ_PIS_REAIS=float(row[34]),
                        VL_PIS=float(row[35]),
                        CST_COFINS=row[36],
                        VL_BC_COFINS=float(row[37]),
                        ALIQ_COFINS_PERC=float(row[38]),
                        QUANT_BC_COFINS=float(row[39]),
                        ALIQ_COFINS_REAIS=float(row[40]),
                        VL_COFINS=float(row[41]),
                        COD_CTA=row[42],
                        VL_ABAT_NT=float(row[43])
                    )
                    reg_c170.save()
                except ValueError as e:
                    self.stdout.write(self.style.ERROR(f'Error importing row: {row}. {e}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully imported data from {file_path} to RegC170 model'))