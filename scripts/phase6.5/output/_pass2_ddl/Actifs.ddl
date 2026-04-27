8e398c8d-bf0d-4fec-b393-61a10c557d57
---
ADD COLUMN "est rattachÃ© Ã  (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'comprend (actifs)' 'syn_7354980190');
ADD COLUMN "est hÃ©bergÃ© dans (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'hÃ©berge (actifs)' 'syn_7839367943');
ADD COLUMN "est utilisÃ© par (collectifs)" RELATION('86af5eb1-d46d-4d8b-ae69-cfc4488fc262', DUAL 'utilise (actifs)' 'syn_3434935278');
ADD COLUMN "est administrÃ© par (collectifs)" RELATION('86af5eb1-d46d-4d8b-ae69-cfc4488fc262', DUAL 'administre (actifs)' 'syn_7464402312');
ADD COLUMN "est utilisÃ© pour rÃ©aliser (actions dÃ©tectÃ©es)" RELATION('eefcb09b-253c-46e6-b67c-7a5d28863ff0', DUAL 'utilise (actifs)' 'syn_3408115554');
ADD COLUMN "est mobilisÃ© par (processus candidats)" RELATION('8f11ed44-18dc-4e89-9baa-70e3c849e253', DUAL 'mobilise (actifs)' 'syn_8423408584');
ADD COLUMN "est utilisÃ© par (processus)" RELATION('d7cf0f34-efe1-467e-8912-65f61a4a1f14', DUAL 'utilise (actifs)' 'syn_6297948041');
ADD COLUMN "est produit par (processus)" RELATION('d7cf0f34-efe1-467e-8912-65f61a4a1f14', DUAL 'produit (actifs)' 'syn_371788000');
ADD COLUMN "est mobilisÃ© par (pratiques organisationnelles)" RELATION('00e31d97-9ae0-4304-b821-71d41aead7b6', DUAL 'mobilise (actifs)' 'syn_3087850154');
ADD COLUMN "est concernÃ© par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'concerne (actifs)' 'syn_7562826790');
ADD COLUMN "concerne (initiatives organisationnelles)" RELATION('02a9770a-a9cd-43aa-90aa-90f11f5523cf', DUAL 'concerne (actifs)' 'syn_815939126');
ADD COLUMN "est concernÃ© par (modulateurs)" RELATION('2172c9b9-c0e5-47eb-942d-5894a553f82a', DUAL 'porte sur (actifs)' 'syn_1278424906')