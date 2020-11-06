<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>506</width>
    <height>531</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="verticalLayoutWidget_3">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>20</y>
     <width>481</width>
     <height>471</height>
    </rect>
   </property>
   <layout class="QVBoxLayout" name="verticalLayout_3">
    <item>
     <widget class="QTabWidget" name="receiverType">
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="tab">
       <attribute name="title">
        <string>Şirket</string>
       </attribute>
       <widget class="QWidget" name="verticalLayoutWidget">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>20</y>
          <width>431</width>
          <height>291</height>
         </rect>
        </property>
        <layout class="QVBoxLayout" name="verticalLayout">
         <item>
          <widget class="QLabel" name="label">
           <property name="text">
            <string>Şirket adı</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLineEdit" name="lineEdit"/>
         </item>
         <item>
          <widget class="QLabel" name="label_2">
           <property name="text">
            <string>Şirket kariyer sayfası</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLineEdit" name="lineEdit_2"/>
         </item>
         <item>
          <widget class="QLabel" name="label_3">
           <property name="text">
            <string>Şirket bilgileri</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QTextEdit" name="textEdit"/>
         </item>
        </layout>
       </widget>
      </widget>
      <widget class="QWidget" name="tab_2">
       <attribute name="title">
        <string>Kişi</string>
       </attribute>
       <widget class="QWidget" name="verticalLayoutWidget_2">
        <property name="geometry">
         <rect>
          <x>20</x>
          <y>20</y>
          <width>421</width>
          <height>291</height>
         </rect>
        </property>
        <layout class="QVBoxLayout" name="verticalLayout_2">
         <item>
          <widget class="QLabel" name="label_4">
           <property name="text">
            <string>Kişi adı</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLineEdit" name="lineEdit_3"/>
         </item>
         <item>
          <widget class="QLabel" name="label_5">
           <property name="text">
            <string>Kişi mail adresi</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QLineEdit" name="lineEdit_4"/>
         </item>
         <item>
          <widget class="QLabel" name="label_6">
           <property name="text">
            <string>Kişi bilgileri</string>
           </property>
          </widget>
         </item>
         <item>
          <widget class="QTextEdit" name="textEdit_2"/>
         </item>
        </layout>
       </widget>
      </widget>
     </widget>
    </item>
    <item>
     <widget class="QPushButton" name="pushButton">
      <property name="minimumSize">
       <size>
        <width>0</width>
        <height>50</height>
       </size>
      </property>
      <property name="font">
       <font>
        <family>Yu Gothic UI</family>
        <pointsize>10</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">background: #3bb865;
color:white;
border-radius:15px;</string>
      </property>
      <property name="text">
       <string>Başvuru oluştur!</string>
      </property>
     </widget>
    </item>
    <item>
     <spacer name="verticalSpacer">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="sizeType">
       <enum>QSizePolicy::Fixed</enum>
      </property>
      <property name="sizeHint" stdset="0">
       <size>
        <width>5</width>
        <height>20</height>
       </size>
      </property>
     </spacer>
    </item>
    <item>
     <widget class="QProgressBar" name="progressBar">
      <property name="font">
       <font>
        <pointsize>14</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">QProgressBar
{
border: solid grey;
border-radius: 15px;
color: black;
}
QProgressBar::chunk 
{
background-color: #05B8CC;
border-radius :15px;
}      </string>
      </property>
      <property name="value">
       <number>78</number>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
      <property name="textVisible">
       <bool>true</bool>
      </property>
      <property name="orientation">
       <enum>Qt::Horizontal</enum>
      </property>
      <property name="invertedAppearance">
       <bool>false</bool>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
