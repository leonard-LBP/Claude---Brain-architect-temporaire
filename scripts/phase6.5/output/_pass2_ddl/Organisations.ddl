ceaf07f7-0809-4428-8d31-9db52d87bf33
---
ADD COLUMN "a pour enfants (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'est enfant de (organisations)' 'syn_3437489666');
ADD COLUMN "est enfant de (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'a pour enfants (organisations)' 'syn_5118947105');
ADD COLUMN "comprend (postes)" RELATION('d1871545-d33e-481c-9813-ce15336aac67', DUAL 'est rattachÃ© Ã  (organisations)' 'syn_6729289791');
ADD COLUMN "est concernÃ©e par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'concerne (organisations)' 'syn_6377388759');
ADD COLUMN "est concernÃ©e par (processus candidats)" RELATION('8f11ed44-18dc-4e89-9baa-70e3c849e253', DUAL 'concerne (organisations)' 'syn_4984442554');
ADD COLUMN "est concernÃ©e par (processus)" RELATION('d7cf0f34-efe1-467e-8912-65f61a4a1f14', DUAL 'concerne (organisations)' 'syn_6694307913');
ADD COLUMN "met en Å“uvre (pratiques organisationnelles)" RELATION('00e31d97-9ae0-4304-b821-71d41aead7b6', DUAL 'est observÃ©e dans (organisations)' 'syn_92104494');
ADD COLUMN "porte (principes organisationnels)" RELATION('00349e89-05d9-4dfd-be7c-534e7844da88', DUAL 'sâ€™applique Ã  (organisations)' 'syn_7868195404');
ADD COLUMN "est concernÃ©e par (problÃ©matiques)" RELATION('e76e6c3e-95f8-476d-a506-9127eb2ca4c2', DUAL 'concerne (organisations)' 'syn_9305015368');
ADD COLUMN "est source de (relations inter-organisations)" RELATION('e87dade3-7806-466b-961d-6c0449857d99', DUAL 'a pour source (organisations)' 'syn_6764575497');
ADD COLUMN "est cible de (relations inter-organisations)" RELATION('e87dade3-7806-466b-961d-6c0449857d99', DUAL 'a pour cible (organisations)' 'syn_684038106')