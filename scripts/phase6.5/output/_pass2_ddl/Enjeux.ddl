eecdfc29-cedf-481f-8cd4-4d0ae52e23cc
---
ADD COLUMN "est exprimÃ© par (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'exprime (enjeux)' 'syn_9948098487');
ADD COLUMN "est exprimÃ© par (individus)" RELATION('fd19eb5d-b866-4b38-9bb9-20e3c3c683ae', DUAL 'exprime (enjeux)' 'syn_5745579655');
ADD COLUMN "est signalÃ© par (journal des signaux)" RELATION('9f429a5c-518d-4e13-a57e-10c5ede57e86', DUAL 'alimente (enjeux)' 'syn_7569041087');
ADD COLUMN "se situe dans (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'contextualise (enjeux)' 'syn_6404594114');
ADD COLUMN "est contextualisÃ© par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'contextualise (enjeux)' 'syn_5347966322');
ADD COLUMN "se consolide en (problÃ©matiques)" RELATION('e76e6c3e-95f8-476d-a506-9127eb2ca4c2', DUAL 'provient de (enjeux)' 'syn_3064138758');
ADD COLUMN "se traduit en (OKR)" RELATION('09e20d61-0443-4b25-a8f4-fe8f57024637', DUAL 'traduit (enjeux)' 'syn_6795819562')