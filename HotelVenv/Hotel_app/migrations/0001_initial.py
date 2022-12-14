# Generated by Django 4.1.3 on 2022-11-18 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblhabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('disponibilidad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='tblhotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblciudad')),
            ],
        ),
        migrations.CreateModel(
            name='tblpais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblprecio_habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='tblservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_servicio', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='tbltemporada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_temp', models.CharField(max_length=200)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='tbltipo_habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_habitacion', models.CharField(max_length=200)),
                ('cant_camas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tbltipo_pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_pago', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblreservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('fecha_llegada', models.DateField()),
                ('hora_llegada', models.TimeField()),
                ('fecha_salida', models.DateField()),
                ('hora_salida', models.TimeField()),
                ('fecha_registro', models.DateField()),
                ('habitacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhabitacion')),
                ('hotel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhotel')),
                ('precio_hab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblprecio_habitacion')),
            ],
        ),
        migrations.AddField(
            model_name='tblprecio_habitacion',
            name='temporda_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltemporada'),
        ),
        migrations.AddField(
            model_name='tblprecio_habitacion',
            name='tipo_habitacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_habitacion'),
        ),
        migrations.CreateModel(
            name='tblpago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reservacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblreservacion')),
                ('servicio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblservicio')),
                ('tipo_pago_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_pago')),
            ],
        ),
        migrations.AddField(
            model_name='tblhotel',
            name='pais_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblpais'),
        ),
        migrations.AddField(
            model_name='tblhabitacion',
            name='hotel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhotel'),
        ),
        migrations.AddField(
            model_name='tblhabitacion',
            name='tipo_habitacion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tbltipo_habitacion'),
        ),
        migrations.CreateModel(
            name='tblcliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default='0')),
                ('identificacion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('habitacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblhabitacion')),
                ('reservacion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hotel_app.tblreservacion')),
            ],
        ),
    ]
