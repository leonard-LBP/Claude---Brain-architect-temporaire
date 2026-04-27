51eaf391-05b3-4276-b8f5-6010dc8a0287
---
ADD COLUMN "a pour enfants (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'est enfant de (environnements)' 'syn_9189314786');
ADD COLUMN "est enfant de (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'a pour enfants (environnements)' 'syn_7746031057');
ADD COLUMN "est voisin de (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'est voisin de (environnements)' 'syn_9079935676');
ADD COLUMN "est voisin de (environnements)" RELATION('51eaf391-05b3-4276-b8f5-6010dc8a0287', DUAL 'est voisin de (environnements)' 'syn_9079935676');
ADD COLUMN "concerne (organisations)" RELATION('ceaf07f7-0809-4428-8d31-9db52d87bf33', DUAL 'est concernÃ©e par (environnements)' 'syn_5707363891');
ADD COLUMN "concerne (individus)" RELATION('fd19eb5d-b866-4b38-9bb9-20e3c3c683ae', DUAL 'est concernÃ© par (environnements)' 'syn_2074619427');
ADD COLUMN "est concernÃ© par (Ã©vÃ©nements)" RELATION('e5aaaac9-5eb3-4bcc-a10a-73e9891100da', DUAL 'concerne (environnements)' 'syn_4105988948');
ADD COLUMN "concerne (initiatives organisationnelles)" RELATION('02a9770a-a9cd-43aa-90aa-90f11f5523cf', DUAL 'se dÃ©ploie dans (environnements)' 'syn_5601409929');
ADD COLUMN "concerne (processus candidats)" RELATION('8f11ed44-18dc-4e89-9baa-70e3c849e253', DUAL 'se dÃ©ploie dans (environnements)' 'syn_629557062');
ADD COLUMN "concerne (processus)" RELATION('d7cf0f34-efe1-467e-8912-65f61a4a1f14', DUAL 'se dÃ©roule dans (environnements)' 'syn_7069390619');
ADD COLUMN "concerne (pratiques organisationnelles)" RELATION('00e31d97-9ae0-4304-b821-71d41aead7b6', DUAL 'se dÃ©ploie dans (environnements)' 'syn_1822370862');
ADD COLUMN "concerne (problÃ©matiques)" RELATION('e76e6c3e-95f8-476d-a506-9127eb2ca4c2', DUAL 'se dÃ©ploie dans (environnements)' 'syn_1909550734')