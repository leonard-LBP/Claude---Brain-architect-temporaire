86af5eb1-d46d-4d8b-ae69-cfc4488fc262
---
ADD COLUMN "a pour enfants (collectifs)" RELATION('86af5eb1-d46d-4d8b-ae69-cfc4488fc262', DUAL 'est enfant de (collectifs)' 'syn_1305727563');
ADD COLUMN "est enfant de (collectifs)" RELATION('86af5eb1-d46d-4d8b-ae69-cfc4488fc262', DUAL 'a pour enfants (collectifs)' 'syn_9013918257');
ADD COLUMN "appartient Ã  (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'comprend (collectifs)' 'syn_2510085473');
ADD COLUMN "a pour membres (individus)" RELATION('fd19eb5d-b866-4b38-9bb9-20e3c3c683ae', DUAL 'est membre de (collectifs)' 'syn_4704071933');
ADD COLUMN "comprend (postes)" RELATION('d1871545-d33e-481c-9813-ce15336aac67', DUAL 'est rattachÃ© Ã  (collectifs)' 'syn_5480794453');
ADD COLUMN "est concernÃ© par (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'concerne (collectifs)' 'syn_8766889927');
ADD COLUMN "est concernÃ© par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'concerne (collectifs)' 'syn_1141955171');
ADD COLUMN "conduit (initiatives organisationnelles)" RELATION('02a9770a-a9cd-43aa-90aa-90f11f5523cf', DUAL 'est conduite par (collectifs)' 'syn_608855211');
ADD COLUMN "exprime (enjeux)" RELATION('eecdfc29-cedf-481f-8cd4-4d0ae52e23cc', DUAL 'est exprimÃ© par (collectifs)' 'syn_3149520016');
ADD COLUMN "met en Å“uvre (pratiques organisationnelles)" RELATION('00e31d97-9ae0-4304-b821-71d41aead7b6', DUAL 'est mise en Å“uvre par (collectifs)' 'syn_3236989305');
ADD COLUMN "est affectÃ© par (problÃ©matiques)" RELATION('e76e6c3e-95f8-476d-a506-9127eb2ca4c2', DUAL 'affecte (collectifs)' 'syn_1451946550');
ADD COLUMN "porte (OKR)" RELATION('09e20d61-0443-4b25-a8f4-fe8f57024637', DUAL 'est portÃ© par (collectifs)' 'syn_6018858803');
ADD COLUMN "est mesurÃ© par (indicateurs)" RELATION('fe9b200f-97c7-4805-9710-5a821d538d0b', DUAL 'mesure la performance de (collectifs)' 'syn_7957478502');
ADD COLUMN "applique (principes organisationnels)" RELATION('00349e89-05d9-4dfd-be7c-534e7844da88', DUAL 'sâ€™applique Ã  (collectifs)' 'syn_887850967')