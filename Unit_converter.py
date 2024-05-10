from PyQt6.QtWidgets import(
    QApplication,QWidget,QLineEdit,QLabel
    ,QGridLayout,QPushButton,QComboBox)
from PyQt6.QtGui import  QFont,QIntValidator
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import sys
select_list=None
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unit converter")
        self.resize(400,500)
        layout=QGridLayout()
        self.setLayout(layout)
        self.quantity=QComboBox()
        self.quantity.setMinimumHeight(10)
        self.amount=QLineEdit()
        self.amount.setValidator(QIntValidator())
        self.unit_primitive=QComboBox()
        self.unit_secondary=QComboBox()
        self.change=QPushButton("Convert")
        self.change.pressed.connect(self.change_unit)
        self.amount.setPlaceholderText("input amount of ...")
        self.quantities = ['Length', 'Area', 'Volume', 'Time', 'Speed', 'Mass', 'Temperature', 'Pressure', 'Energy', 'Power', 'Force', 'Angle', 'Frequency', 'Electric Current', 'Voltage', 'Resistance', 'Capacitance', 'Inductance', 'Electric Charge', 'Electric Potential', 'Electric Conductance', 'Magnetic Flux', 'Magnetic Flux Density', 'Luminous Intensity', 'Illuminance', 'Radioactivity', 'Absorbed Dose', 'Equivalent Dose', 'Catalytic Activity']
        pi=3.14
        length_units = [
    ("meter", 1), # SI base unit
    ("kilometer", 1000),
    ("centimeter", 0.01),
    ("millimeter", 0.001),
    ("micrometer", 1e-6),
    ("nanometer", 1e-9),
    ("picometer", 1e-12),
    ("femtometer", 1e-15),
    ("inch", 0.0254),
    ("foot", 0.3048),
    ("yard", 0.9144),
    ("mile", 1609.344),
    ("nautical mile", 1852),
    ("fathom", 1.8288),
    ("rod", 5.0292),
    ("chain", 20.1168),
    ("furlong", 201.168),
    ("astronomical unit", 1.496e11),
    ("light year", 9.461e15),
    ("parsec", 3.086e16)
]
        global select_list
        select_list=length_units
        area_units = [
    ("square meter", 1), # SI derived unit
    ("square kilometer", 1e6),
    ("square centimeter", 1e-4),
    ("square millimeter", 1e-6),
    ("square micrometer", 1e-12),
    ("square nanometer", 1e-18),
    ("square picometer", 1e-24),
    ("square inch", 0.00064516),
    ("square foot", 0.092903),
    ("square yard", 0.836127),
    ("square mile", 2.58999e6),
    ("acre", 4046.86),
    ("hectare", 1e4),
    ("are", 100)
]
        # SI unit of volume is cubic meter (m^3)
        volume_units = [
    ("cubic meter", 1), # SI derived unit
    ("cubic kilometer", 1e9),
    ("cubic centimeter", 1e-6),
    ("cubic millimeter", 1e-9),
    ("cubic micrometer", 1e-18),
    ("cubic nanometer", 1e-27),
    ("cubic picometer", 1e-36),
    ("liter", 0.001), # special name for cubic decimeter
    ("milliliter", 1e-6), # special name for cubic centimeter
    ("cubic inch", 0.000016387064),
    ("cubic foot", 0.028316846592),
    ("cubic yard", 0.764554857984),
    ("cubic mile", 4.168181825440579e9),
    ("gallon (US)", 0.003785411784),
    ("gallon (UK)", 0.00454609),
    ("barrel (oil)", 0.158987294928)
]

# SI unit of time is second (s)
        time_units = [
    ("second", 1), # SI base unit
    ("millisecond", 0.001),
    ("microsecond", 1e-6),
    ("nanosecond", 1e-9),
    ("picosecond", 1e-12),
    ("femtosecond", 1e-15),
    ("minute", 60),
    ("hour", 3600),
    ("day", 86400),
    ("week", 604800),
    ("month", 2629800), # average of 30.44 days
    ("year", 31557600), # average of 365.24 days
    ("decade", 315576000), # 10 years
    ("century", 3155760000), # 100 years
    ("millennium", 31557600000), # 1000 years
]
        # SI unit of speed is meter per second (m/s)
        speed_units = [
    ("meter per second", 1), # SI derived unit
    ("kilometer per hour", 0.277778),
    ("mile per hour", 0.44704),
    ("knot", 0.514444),
    ("mach", 340.3), # speed of sound in air at sea level
    ("light", 299792458) # speed of light in vacuum
]

# SI unit of mass is kilogram (kg)
        mass_units = [
    ("am", 1), # SI base unit
    ("gram", 0.001),
    ("milligram", 1e-6),
    ("microgram", 1e-9),
    ("tonne", 1000),
    ("pound", 0.453592),
    ("ounce", 0.0283495),
    ("stone", 6.35029),
    ("electronvolt", 1.782662e-36), # mass-energy equivalence
    ("atomic mass unit", 1.660539e-27) # 1/12 of the mass of a carbon-12 atom
]

# SI unit of temperature is kelvin (K)
        temperature_units = [
    ("kelvin", 1), # SI base unit
    ("celsius", lambda x: x + 273.15), # conversion function from celsius to kelvin
    ("fahrenheit", lambda x: (x + 459.67) * 5/9), # conversion function from fahrenheit to kelvin
    ("rankine", 0.555556),
    ("newton", 3.030303),
    ("rømer", 1.904761),
    ("réaumur", 1.25),
    ("delisle", -0.666667)
]
# SI unit of pressure is pascal (Pa)
        pressure_units = [
    ("pascal", 1), # SI base unit
    ("bar", 1e5),
    ("atmosphere", 101325),
    ("torr", 133.322),
    ("millimeter of mercury", 133.322),
    ("pound per square inch", 6894.76),
    ("barye", 0.1),
    ("kilopascal", 1000),
    ("megapascal", 1e6),
    ("gigapascal", 1e9)
]

# SI unit of energy is joule (J)
        energy_units = [
    ("joule", 1), # SI derived unit
    ("erg", 1e-7),
    ("calorie", 4.184),
    ("kilocalorie", 4184),
    ("watt hour", 3600),
    ("kilowatt hour", 3.6e6),
    ("electronvolt", 1.602176634e-19),
    ("british thermal unit", 1055.06),
    ("foot pound", 1.35582),
    ("ton of TNT", 4.184e9)
]

# SI unit of power is watt (W)
        power_units = [
    ("watt", 1), # SI derived unit
    ("kilowatt", 1000),
    ("megawatt", 1e6),
    ("gigawatt", 1e9),
    ("terawatt", 1e12),
    ("horsepower", 745.7),
    ("foot pound per second", 1.35582),
    ("calorie per second", 4.184),
    ("kilocalorie per hour", 1.16222),
    ("british thermal unit per hour", 0.293071)
]
# SI unit of force is newton (N)
        force_units = [
    ("newton", 1), # SI derived unit
    ("dyne", 1e-5),
    ("pound-force", 4.44822),
    ("kilogram-force", 9.80665),
    ("kip", 4448.22),
    ("ton-force", 8896.44)
]

# SI unit of angle is radian (rad)
        angle_units = [
    ("radian", 1), # SI derived unit
    ("degree", pi/180), # conversion factor from degree to radian
    ("gradian", pi/200), # conversion factor from gradian to radian
    ("minute of arc", pi/10800), # conversion factor from minute of arc to radian
    ("second of arc", pi/648000), # conversion factor from second of arc to radian
    ("revolution", 2*pi) # conversion factor from revolution to radian
]

# SI unit of frequency is hertz (Hz)
        frequency_units = [
    ("hertz", 1), # SI derived unit
    ("kilohertz", 1000),
    ("megahertz", 1e6),
    ("gigahertz", 1e9),
    ("terahertz", 1e12),
    ("radian per second", 1/(2*pi)), # conversion factor from radian per second to hertz
    ("revolution per minute", 1/60) # conversion factor from revolution per minute to hertz
]
# SI unit of electric current is ampere (A)
        current_units = [
    ("ampere", 1), # SI base unit
    ("milliampere", 0.001),
    ("microampere", 1e-6),
    ("kiloampere", 1000),
    ("abampere", 10) # CGS unit
]

# SI unit of voltage is volt (V)
        voltage_units = [
    ("volt", 1), # SI derived unit
    ("millivolt", 0.001),
    ("microvolt", 1e-6),
    ("kilovolt", 1000),
    ("megavolt", 1e6),
    ("gigavolt", 1e9),
    ("abvolt", 1e-8) # CGS unit
]

# SI unit of resistance is ohm (Ω)
        resistance_units = [
    ("ohm", 1), # SI derived unit
    ("milliohm", 0.001),
    ("microohm", 1e-6),
    ("kiloohm", 1000),
    ("megaohm", 1e6),
    ("gigaohm", 1e9),
    ("abohm", 1e-9) # CGS unit
]
# SI unit of capacitance is farad (F)
        capacitance_units = [
    ("farad", 1), # SI derived unit
    ("microfarad", 1e-6),
    ("nanofarad", 1e-9),
    ("picofarad", 1e-12),
    ("femtofarad", 1e-15),
    ("abfarad", 1e9), # CGS unit
    ("statfarad", 1.1126e-12) # CGS unit
]

# SI unit of inductance is henry (H)
        inductance_units = [
    ("henry", 1), # SI derived unit
    ("millihenry", 0.001),
    ("microhenry", 1e-6),
    ("nanohenry", 1e-9),
    ("abhenry", 1e-9), # CGS unit
    ("stathenry", 8.9876e11) # CGS unit
]
        conductance_units = [
("siemens", 1), # SI base unit
("kilosiemens", 1000),
("millisiemens", 0.001),
("microsiemens", 1e-6),
("nanosiemens", 1e-9),
("picosiemens", 1e-12),
("femtosiemens", 1e-15),
("mho", 1),
("abmho", 1e9),
("statmho", 1.112650056e-12)
        ]
        flux_units = [
("weber", 1), # SI base unit
("kiloweber", 1000),
("milliweber", 0.001),
("microweber", 1e-6),
("nanoweber", 1e-9),
("picoweber", 1e-12),
("femtoweber", 1e-15),
("maxwell", 1e-8),
("unit pole", 1.256637062e-7)
        ]
# SI unit of electric charge is coulomb (C)
        charge_units = [
    ("coulomb", 1), # SI derived unit
    ("millicoulomb", 0.001),
    ("microcoulomb", 1e-6),
    ("nanocoulomb", 1e-9),
    ("picocoulomb", 1e-12),
    ("elementary charge", 1.602176634e-19), # charge of a proton or electron
    ("faraday", 96485.33212), # charge of a mole of electrons
    ("ampere-hour", 3600), # charge delivered by a current of one ampere in one hour
]
        potential_units = [
("volt", 1), # SI base unit
("kilovolt", 1000),
("millivolt", 0.001),
("microvolt", 1e-6),
("nanovolt", 1e-9),
("picovolt", 1e-12),
("femtovolt", 1e-15),
("abvolt", 1e-8),
("statvolt", 299.792458)
        ]
        density_units = [
("tesla", 1), # SI base unit
("kilotesla", 1000),
("millitesla", 0.001),
("microtesla", 1e-6),
("nanotesla", 1e-9),
("picotesla", 1e-12),
("femtotesla", 1e-15),
("gauss", 1e-4)
        ]
        intensity_units = [
("candela", 1), # SI base unit
("millicandela", 0.001),
("microcandela", 1e-6),
("nanocandela", 1e-9),
("picocandela", 1e-12),
("femtocandela", 1e-15),
("lumen", 1),
("nit", 1)]
        illuminance_units = [
("lux", 1), # SI base unit
("kilolux", 1000),
("millilux", 0.001),
("microlux", 1e-6),
("nanolux", 1e-9),
("picolux", 1e-12),
("femtolux", 1e-15),
("phot", 1e4),
("foot-candle", 10.76391)
        ]
        radioactivity_units = [
("becquerel", 1), # SI base unit
("kilobecquerel", 1000),
("megabecquerel", 1e6),
("gigabecquerel", 1e9),
("curie", 3.7e10),
("millicurie", 3.7e7),
("microcurie", 3.7e4),
("picocurie", 3.7e-2),
("rutherford", 1e6)
        ]
        absorbed_dose_units = [
("gray", 1), # SI base unit
("kilogray", 1000),
("milligray", 0.001),
("microgray", 1e-6),
("nanogray", 1e-9),
("picogray", 1e-12),
("rad", 0.01),
("millirad", 1e-5),
("microrad", 1e-8)
        ]
        equivalent_dose_units = [
("sievert", 1), # SI base unit
("kilosievert", 1000),
("millisievert", 0.001),
("microsievert", 1e-6),
("nanosievert", 1e-9),
("picosievert", 1e-12),
("rem", 0.01),
("millirem", 1e-5),
("microrem", 1e-8)
        ]
        catalytic_activity_units = [
("katal", 1), # SI base unit
("kilokatal", 1000),
("millikatal", 0.001),
("microkatal", 1e-6),
("nanokatal", 1e-9),
("picokatal", 1e-12),
("enzyme unit", 16.67e-9),
("milli enzyme unit", 16.67e-12),
("micro enzyme unit", 16.67e-15)
        ]
        self.unit=[length_units,area_units,volume_units,time_units,speed_units,mass_units,temperature_units,pressure_units,energy_units,power_units,force_units,
                   angle_units,frequency_units,current_units,voltage_units,resistance_units,capacitance_units,inductance_units,conductance_units,flux_units,
                   charge_units,potential_units,density_units,intensity_units,illuminance_units,radioactivity_units,absorbed_dose_units,equivalent_dose_units,catalytic_activity_units]
        self.result=QLabel()
        self.result.setMaximumHeight(18)
        self.result.setMinimumWidth(2)
        self.result.setFont(QFont("Arial Bold",16))
        self.quantity.addItems(self.quantities)
        self.quantity.currentTextChanged.connect(self.change_quantity)
        for i in range(len(length_units)):
            self.unit_primitive.addItem(length_units[i][0])
        for i in range(len(length_units)):
            self.unit_secondary.addItem(length_units[i][0])
        layout.addWidget(self.quantity,0,0)
        layout.addWidget(self.amount,1,0)
        layout.addWidget(self.unit_primitive,2,0)
        layout.addWidget(self.unit_secondary,3,0)
        layout.addWidget(self.change,4,0)
        layout.addWidget(self.result,5,0)
        self.selected=None
        self.change=None
    def change_quantity(self,text):
        count=1
      
        for i in range(29):
            if text==self.quantities[count]:
                self.unit_primitive.clear()
                self.unit_secondary.clear()            
                for i in range(len(self.unit[count])):
                   self.unit_primitive.addItem(self.unit[count][i][0])
                   self.unit_secondary.addItem(self.unit[count][i][0])
                global select_list
                select_list=self.unit[count]
                
                break
            else:
                count=count+1
    def change_unit(self):
        
        p=self.unit_primitive.currentText()
        s=self.unit_secondary.currentText()
        amount=self.amount.text()
        p_value=None
        s_value=None
        try:
            amount=int(amount)
        except:
             pass
        global select_list
        for unit, value in select_list:
            if unit == p:
                p_value=value
                break
        for unit, value in select_list:
            if unit == s:
                s_value=value
                break
        result=None
        if p_value<s_value:
            result=str((amount*p_value)/s_value)
        else:
            result=str((amount*p_value)/s_value)
        self.result.setText(result)
app=QApplication(sys.argv)
window=Window()
window.show()
app.exec()



