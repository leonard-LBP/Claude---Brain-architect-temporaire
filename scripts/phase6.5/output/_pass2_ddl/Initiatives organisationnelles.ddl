02a9770a-a9cd-43aa-90aa-90f11f5523cf
---
ADD COLUMN "comprend (initiatives organisationnelles)" RELATION('02a9770a-a9cd-43aa-90aa-90f11f5523cf', DUAL 'est incluse dans (initiatives organisationnelles)' 'syn_5039312002');
ADD COLUMN "est incluse dans (initiatives organisationnelles)" RELATION('02a9770a-a9cd-43aa-90aa-90f11f5523cf', DUAL 'comprend (initiatives organisationnelles)' 'syn_5792810457');
ADD COLUMN "est portÃ©e par (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'porte (initiatives organisationnelles)' 'syn_9590883563');
ADD COLUMN "est sponsorisÃ©e par (postes)" RELATION('d1871545-d33e-481c-9813-ce15336aac67', DUAL 'sponsorise (initiatives organisationnelles)' 'syn_7286777121');
ADD COLUMN "est jalonnÃ©e par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'jalonne (initiatives organisationnelles)' 'syn_4300747549');
ADD COLUMN "adresse (problÃ©matiques)" RELATION('e76e6c3e-95f8-476d-a506-9127eb2ca4c2', DUAL 'est adressÃ©e par (initiatives organisationnelles)' 'syn_9416151644');
ADD COLUMN "contribue Ã  (OKR)" RELATION('09e20d61-0443-4b25-a8f4-fe8f57024637', DUAL 'est servi par (initiatives organisationnelles)' 'syn_6142511593')