FasdUAS 1.101.10   ��   ��    k             l     ��  ��    7 1set root to (container of (path to me)) as string     � 	 	 b s e t   r o o t   t o   ( c o n t a i n e r   o f   ( p a t h   t o   m e ) )   a s   s t r i n g   
  
 l     ��  ��    = 7set current_path to container of (path to me) as string     �   n s e t   c u r r e n t _ p a t h   t o   c o n t a i n e r   o f   ( p a t h   t o   m e )   a s   s t r i n g      l    	 ����  r     	    l     ����  I    ��  
�� .earsffdralis        afdr   f       �� ��
�� 
rtyp  m    ��
�� 
TEXT��  ��  ��    o      ���� 0 current_path  ��  ��        l  
  ����  r   
     n   
     1    ��
�� 
psxp  o   
 ���� 0 current_path    o      ���� 0 pos_path  ��  ��         l     ��������  ��  ��      ! " ! l   � #���� # O    � $ % $ k    � & &  ' ( ' I   ������
�� .miscactvnull��� ��� null��  ��   (  ) * ) l   �� + ,��   + 2 ,set currentTab to do script ("cd ~/Desktop")    , � - - X s e t   c u r r e n t T a b   t o   d o   s c r i p t   ( " c d   ~ / D e s k t o p " ) *  . / . l   �� 0 1��   0 A ;set window_id to id of first window whose frontmost is true    1 � 2 2 v s e t   w i n d o w _ i d   t o   i d   o f   f i r s t   w i n d o w   w h o s e   f r o n t m o s t   i s   t r u e /  3 4 3 r    ! 5 6 5 b     7 8 7 m     9 9 � : :  d i r = 8 n     ; < ; 1    ��
�� 
strq < o    ���� 0 pos_path   6 o      ���� 0 commandtorun1 commandToRun1 4  = > = r   " % ? @ ? m   " # A A � B B ( c d   $ ( d i r n a m e   " $ d i r " ) @ o      ���� 0 commandtorun2 commandToRun2 >  C D C r   & ) E F E m   & ' G G � H H 
 c d   . . F o      ���� 0 commandtorun3 commandToRun3 D  I J I r   * / K L K m   * + M M � N N . s o u r c e   e n v / b i n / a c t i v a t e L o      ���� 0 commandtorun4 commandToRun4 J  O P O r   0 7 Q R Q m   0 3 S S � T T 4 p y t h o n   m a n a g e . p y   r u n s e r v e r R o      ���� 0 commandtorun5 commandToRun5 P  U V U l  8 8�� W X��   W N Hdo script commandToRun1 in window id window_id of application "Terminal"    X � Y Y � d o   s c r i p t   c o m m a n d T o R u n 1   i n   w i n d o w   i d   w i n d o w _ i d   o f   a p p l i c a t i o n   " T e r m i n a l " V  Z [ Z r   8 A \ ] \ I  8 =�� ^��
�� .coredoscnull��� ��� ctxt ^ o   8 9���� 0 commandtorun1 commandToRun1��   ] o      ���� 0 
currenttab 
currentTab [  _ ` _ I  B G�� a��
�� .sysodelanull��� ��� nmbr a m   B C���� ��   `  b c b I  H S�� d e
�� .coredoscnull��� ��� ctxt d o   H I���� 0 commandtorun2 commandToRun2 e �� f��
�� 
kfil f o   L O���� 0 
currenttab 
currentTab��   c  g h g I  T Y�� i��
�� .sysodelanull��� ��� nmbr i m   T U���� ��   h  j k j I  Z e�� l m
�� .coredoscnull��� ��� ctxt l o   Z [���� 0 commandtorun3 commandToRun3 m �� n��
�� 
kfil n o   ^ a���� 0 
currenttab 
currentTab��   k  o p o I  f k�� q��
�� .sysodelanull��� ��� nmbr q m   f g���� ��   p  r s r I  l y�� t u
�� .coredoscnull��� ��� ctxt t o   l o���� 0 commandtorun4 commandToRun4 u �� v��
�� 
kfil v o   r u���� 0 
currenttab 
currentTab��   s  w x w I  z �� y��
�� .sysodelanull��� ��� nmbr y m   z {���� ��   x  z { z I  � ��� | }
�� .coredoscnull��� ��� ctxt | o   � ����� 0 commandtorun5 commandToRun5 } �� ~��
�� 
kfil ~ o   � ����� 0 
currenttab 
currentTab��   {  ��  I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��  ��   % m     � ��                                                                                      @ alis    >  Macintosh SSD                  BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   S S D  #Applications/Utilities/Terminal.app   / ��  ��  ��   "  � � � l  �! ����� � O   �! � � � k   �  � �  � � � I  � �������
�� .miscactvnull��� ��� null��  ��   �  � � � r   � � � � � b   � � � � � m   � � � � � � �  d i r = � n   � � � � � 1   � ���
�� 
strq � o   � ����� 0 pos_path   � o      ���� 0 commandtorun1 commandToRun1 �  � � � r   � � � � � m   � � � � � � � ( c d   $ ( d i r n a m e   " $ d i r " ) � o      ���� 0 commandtorun2 commandToRun2 �  � � � r   � � � � � m   � � � � � � � 
 c d   . . � o      ���� 0 commandtorun3 commandToRun3 �  � � � r   � � � � � m   � � � � � � � . s o u r c e   e n v / b i n / a c t i v a t e � o      ���� 0 commandtorun4 commandToRun4 �  � � � r   � � � � � m   � � � � � � � 8 s u d o   p y t h o n   n e t w o r k . p y   s t a r t � o      ���� 0 commandtorun5 commandToRun5 �  � � � l  � ��� � ���   � N Hdo script commandToRun1 in window id window_id of application "Terminal"    � � � � � d o   s c r i p t   c o m m a n d T o R u n 1   i n   w i n d o w   i d   w i n d o w _ i d   o f   a p p l i c a t i o n   " T e r m i n a l " �  � � � r   � � � � � I  � ��� ���
�� .coredoscnull��� ��� ctxt � o   � ����� 0 commandtorun1 commandToRun1��   � o      ���� 0 
currenttab 
currentTab �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � I  � ��� � �
�� .coredoscnull��� ��� ctxt � o   � ����� 0 commandtorun2 commandToRun2 � �� ���
�� 
kfil � o   � ����� 0 
currenttab 
currentTab��   �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � I  � ��� � �
�� .coredoscnull��� ��� ctxt � o   � ����� 0 commandtorun3 commandToRun3 � �� ���
�� 
kfil � o   � ����� 0 
currenttab 
currentTab��   �  � � � I  � ��� ���
�� .sysodelanull��� ��� nmbr � m   � ����� ��   �  � � � I  ��� � �
�� .coredoscnull��� ��� ctxt � o   � ����� 0 commandtorun4 commandToRun4 � �� ���
�� 
kfil � o   ����� 0 
currenttab 
currentTab��   �  � � � I �� ���
�� .sysodelanull��� ��� nmbr � m  ���� ��   �  � � � I �� � �
�� .coredoscnull��� ��� ctxt � o  ���� 0 commandtorun5 commandToRun5 � �� ���
�� 
kfil � o  ���� 0 
currenttab 
currentTab��   �  ��� � I  �� ���
�� .sysodelanull��� ��� nmbr � m  ���� ��  ��   � m   � � � ��                                                                                      @ alis    >  Macintosh SSD                  BD ����Terminal.app                                                   ����            ����  
 cu             	Utilities   &/:Applications:Utilities:Terminal.app/    T e r m i n a l . a p p    M a c i n t o s h   S S D  #Applications/Utilities/Terminal.app   / ��  ��  ��   �  �� � l     �~�}�|�~  �}  �|  �       �{ � ��{   � �z
�z .aevtoappnull  �   � **** � �y ��x�w � ��v
�y .aevtoappnull  �   � **** � k    ! � �   � �   � �  ! � �  ��u�u  �x  �w   �   � �t�s�r�q�p�o ��n 9�m�l A�k G�j M�i S�h�g�f�e�d � � � � �
�t 
rtyp
�s 
TEXT
�r .earsffdralis        afdr�q 0 current_path  
�p 
psxp�o 0 pos_path  
�n .miscactvnull��� ��� null
�m 
strq�l 0 commandtorun1 commandToRun1�k 0 commandtorun2 commandToRun2�j 0 commandtorun3 commandToRun3�i 0 commandtorun4 commandToRun4�h 0 commandtorun5 commandToRun5
�g .coredoscnull��� ��� ctxt�f 0 
currenttab 
currentTab
�e .sysodelanull��� ��� nmbr
�d 
kfil�v")��l E�O��,E�O� �*j O���,%E�O�E�O�E�O�E` Oa E` O�j E` Okj O�a _ l Okj O�a _ l Okj O_ a _ l Okj O_ a _ l Okj UO� �*j Oa ��,%E�Oa E�Oa E�Oa E` Oa E` O�j E` Olj O�a _ l Okj O�a _ l Okj O_ a _ l Okj O_ a _ l Okj Uascr  ��ޭ