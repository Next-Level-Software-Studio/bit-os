# # ==============================================================================
# # PROFILE.BASHRC - Esqueleto de Hooks Nativos do Portage
# # Caminho no Overlay: profiles/<nome-do-perfil>/profile.bashrc
# # ==============================================================================

# pkg_pretend() {
#     # Executada antes de qualquer download, extração ou compilação.
#     # Serve exclusivamente para realizar testes de sanidade e validar se o
#     # ambiente cumpre os requisitos mínimos para prosseguir.
    
#     :
# }

# pkg_setup() {
#     # Executada logo após a fase de verificação e antes da compilação.
#     # Serve para preparar o ambiente local, carregar variáveis específicas
#     # e configurar dependências de build necessárias para o ebuild atual.

#     :
# }

# pkg_preinst() {
#     # Executada após o pacote ter sido compilado com sucesso na diretoria
#     # temporária (${D}), mas ANTES de os ficheiros serem movidos para o sistema
#     # de ficheiros real (/). O sistema real ainda não foi modificado.

#     :
# }

# pkg_postinst() {
#     # Executada imediatamente após todos os ficheiros do pacote terem sido
#     # copiados e instalados no sistema real (/). O pacote está oficialmente
#     # ativo e visível no sistema.

#     :
# }

# pkg_prerm() {
#     # Executada quando o processo de desinstalação (unmerge) é iniciado,
#     # mas ANTES de qualquer ficheiro do pacote ser efetivamente apagado do
#     # sistema real (/).

#     :
# }

# pkg_postrm() {
#     # Executada imediatamente após o pacote e todos os seus ficheiros associados
#     # terem sido completamente removidos e limpos do sistema real (/).

#     :
# }
