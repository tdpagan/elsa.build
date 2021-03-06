# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-20 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0008_auto_20180614_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('logical_identifier', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Laboratory', 'Laboratory'), ('Observatory', 'Observatory')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('model_id', models.CharField(max_length=100)),
                ('naif_instrument_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('subtype', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Accelerometer', 'Accelerometer'), ('Alpha Particle Detector', 'Alpha Particle Detector'), ('Alpha Particle X-Ray Spectrometer', 'Alpha Particle X-Ray Spectrometer'), ('Altimeter', 'Altimeter'), ('Anemometer', 'Anemometer'), ('Atmospheric Sciences', 'Atmospheric Sciences'), ('Atomic Force Microscope', 'Atomic Force Microscope'), ('Barometer', 'Barometer'), ('Biology Experiments', 'Biology Experiments'), ('Bolometer', 'Bolometer'), ('Camera', 'Camera'), ('Cosmic Ray Detector', 'Cosmic Ray Detector'), ('Drilling Tool', 'Drilling Tool'), ('Dust', 'Dust'), ('Dust Detector', 'Dust Detector'), ('Electrical Probe', 'Electrical Probe'), ('Energetic Particle Detector', 'Energetic Particle Detector'), ('Gamma Ray Detector', 'Gamma Ray Detector'), ('Gas Analyzer', 'Gas Analyzer'), ('Gravimeter', 'Gravimeter'), ('Grinding Tool', 'Grinding Tool'), ('Hygrometer', 'Hygrometer'), ('Imager', 'Imager'), ('Imaging Spectrometer', 'Imaging Spectrometer'), ('Inertial Measurement Unit', 'Inertial Measurement Unit'), ('Infrared Spectrometer', 'Infrared Spectrometer'), ('Interferometer', 'Interferometer'), ('Laser Induced Breakdown Spectrometer', 'Laser Induced Breakdown Spectrometer'), ('Magnetometer', 'Magnetometer'), ('Mass Spectrometer', 'Mass Spectrometer'), ('Microscope', 'Microscope'), ('Microwave Spectrometer', 'Microwave Spectrometer'), ('Moessbauer Spectrometer', 'Moessbauer Spectrometer'), ('Naked Eye', 'Naked Eye'), ('Neutral Particle Detector', 'Neutral Particle Detector'), ('Neutron Detector', 'Neutron Detector'), ('Particle Detector', 'Particle Detector'), ('Photometer', 'Photometer'), ('Plasma Analyzer', 'Plasma Analyzer'), ('Plasma Detector', 'Plasma Detector'), ('Plasma Wave Spectrometer', 'Plasma Wave Spectrometer'), ('Polarimeter', 'Polarimeter'), ('Radar', 'Radar'), ('Radio Science', 'Radio Science'), ('Radio Spectrometer', 'Radio Spectrometer'), ('Radio Telescope', 'Radio Telescope'), ('Radio-Radar', 'Radio-Radar'), ('Radiometer', 'Radiometer'), ('Reflectometer', 'Reflectometer'), ('Regolith Properties', 'Regolith Properties'), ('Robotic Arm', 'Robotic Arm'), ('Seismometer', 'Seismometer'), ('Small Bodies Sciences', 'Small Bodies Sciences'), ('Spectrograph', 'Spectrograph'), ('Spectrograph Imager', 'Spectrograph Imager'), ('Spectrometer', 'Spectrometer'), ('Thermal Imager', 'Thermal Imager'), ('Thermal Probe', 'Thermal Probe'), ('Thermometer', 'Thermometer'), ('Ultraviolet Spectrometer', 'Ultraviolet Spectrometer'), ('Weather Station', 'Weather Station'), ('Wet Chemistry Laboratory', 'Wet Chemistry Laboratory'), ('X-ray Detector', 'X-ray Detector'), ('X-ray Diffraction Spectrometer', 'X-ray Diffraction Spectrometer'), ('X-ray Fluorescence Spectrometer', 'X-ray Fluorescence Spectrometer')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('naif_host_id', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('satellite', 'satellite'), ('spacecraft', 'spacecraft')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('type_of', models.CharField(choices=[('Asteroid', 'Asteroid'), ('Calibration', 'Calibration'), ('Calibration Field', 'Calibration Field'), ('Calibrator', 'Calibrator'), ('Comet', 'Comet'), ('Dust', 'Dust'), ('Dwarf Planet', 'Dwarf Planet'), ('Equipment', 'Equipment'), ('Exoplanet System', 'Exoplanet System'), ('Galaxy', 'Galaxy'), ('Globular Cluster', 'Globular Cluster'), ('Lunar Sample', 'Lunar Sample'), ('Meteorite', 'Meteorite'), ('Meteoroid', 'Meteoroid'), ('Meteoroid Stream', 'Meteoroid Stream'), ('Nebula', 'Nebula'), ('Open Cluster', 'Open Cluster'), ('Planet', 'Planet'), ('Planetary Nebula', 'Planetary Nebula'), ('Planetary System', 'Planetary System'), ('Plasma Cloud', 'Plasma Cloud'), ('Plasma Stream', 'Plasma Stream'), ('Ring', 'Ring'), ('Satellite', 'Satellite'), ('Star', 'Star'), ('Star Cluster', 'Star Cluster'), ('Sun', 'Sun'), ('Synthetic Sample', 'Synthetic Sample'), ('Terrestrial Sample', 'Terrestrial Sample'), ('Trans-Neptunian Object', 'Trans-Neptunian Object')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TargetAnalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
