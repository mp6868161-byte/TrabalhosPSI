import tkinter as tk
from tkinter import ttk, messagebox

from artista import criar_artista, ler_artistas, atualizar_artista, eliminar_artista
from bilhetes import criar_bilhete, listar_bilhetes, consultar_bilhete, eliminar_bilhete
from staff import criar_staff, listar_staff, atualizar_staff, remover_staff
from concerto import criar_concerto, listar_concertos, atualizar_concerto, eliminar_concerto

# ── PALETA ──────────────────────────────────────────────────────────────────
BG        = "#0D1117"   # fundo principal
SIDEBAR   = "#161B22"   # barra lateral
CARD      = "#21262D"   # cards / frames internos
BORDER    = "#30363D"   # bordas
ACCENT    = "#238636"   # verde GitHub
ACCENT_H  = "#2EA043"   # hover do accent
DANGER    = "#DA3633"   # vermelho (eliminar)
DANGER_H  = "#F85149"
WARNING   = "#D29922"   # amarelo (atualizar)
WARNING_H = "#E3B341"
INFO      = "#1F6FEB"   # azul (consultar)
INFO_H    = "#388BFD"
FG        = "#E6EDF3"   # texto principal
FG2       = "#8B949E"   # texto secundário
FG3       = "#3D444D"   # texto muito apagado
FONT      = "Segoe UI"

# ── ESTILOS ttk ─────────────────────────────────────────────────────────────
def aplicar_estilos():
    s = ttk.Style()
    s.theme_use("clam")
    s.configure("Treeview",
        background=CARD, foreground=FG, fieldbackground=CARD,
        rowheight=30, font=(FONT, 10), borderwidth=0
    )
    s.configure("Treeview.Heading",
        background=SIDEBAR, foreground=FG2, font=(FONT, 10, "bold"),
        relief="flat", borderwidth=0
    )
    s.map("Treeview",
        background=[("selected", ACCENT)],
        foreground=[("selected", FG)]
    )
    s.configure("Vertical.TScrollbar",
        background=BORDER, troughcolor=BG, borderwidth=0, arrowcolor=FG2
    )


# ── BOTÃO MODERNO ────────────────────────────────────────────────────────────
class BotaoModerno(tk.Button):
    def __init__(self, master, texto, cor, cor_hover, comando=None, largura=14, **kw):
        super().__init__(
            master, text=texto, command=comando,
            bg=cor, fg=FG, activebackground=cor_hover, activeforeground=FG,
            font=(FONT, 10, "bold"), relief="flat", bd=0,
            cursor="hand2", width=largura, padx=10, pady=6, **kw
        )
        self._cor = cor
        self._cor_hover = cor_hover
        self.bind("<Enter>", lambda e: self.config(bg=cor_hover))
        self.bind("<Leave>", lambda e: self.config(bg=cor))


# ── DIÁLOGO GENÉRICO ────────────────────────────────────────────────────────
class Dialogo(tk.Toplevel):
    def __init__(self, master, titulo, campos, valores_iniciais=None):
        super().__init__(master)
        self.title(titulo)
        self.configure(bg=BG)
        self.resizable(False, False)
        self.grab_set()

        self.resultado = None
        self.entradas = {}

        # Centrar na janela pai
        self.update_idletasks()
        pw = master.winfo_rootx() + master.winfo_width() // 2
        ph = master.winfo_rooty() + master.winfo_height() // 2
        self.geometry(f"+{pw - 200}+{ph - 150}")

        # Cabeçalho
        tk.Label(self, text=titulo, bg=BG, fg=FG,
                 font=(FONT, 13, "bold"), pady=14).pack(fill="x", padx=20)

        separador = tk.Frame(self, bg=BORDER, height=1)
        separador.pack(fill="x", padx=20)

        frame = tk.Frame(self, bg=BG, padx=24, pady=14)
        frame.pack(fill="both")

        for i, (label, chave) in enumerate(campos):
            tk.Label(frame, text=label, bg=BG, fg=FG2,
                     font=(FONT, 10), anchor="w").grid(row=i, column=0, sticky="w", pady=4)
            e = tk.Entry(frame, bg=CARD, fg=FG, insertbackground=FG,
                         font=(FONT, 10), relief="flat", bd=0,
                         highlightthickness=1, highlightbackground=BORDER,
                         highlightcolor=ACCENT, width=28)
            e.grid(row=i, column=1, padx=(12, 0), pady=4)
            if valores_iniciais and chave in valores_iniciais:
                e.insert(0, valores_iniciais[chave])
            self.entradas[chave] = e

        # Botões
        bf = tk.Frame(self, bg=BG, padx=24, pady=12)
        bf.pack(fill="x")
        BotaoModerno(bf, "Confirmar", ACCENT, ACCENT_H, self._confirmar, largura=12).pack(side="right", padx=(8, 0))
        BotaoModerno(bf, "Cancelar", CARD, BORDER, self.destroy, largura=12).pack(side="right")

    def _confirmar(self):
        self.resultado = {k: v.get().strip() for k, v in self.entradas.items()}
        self.destroy()


# ── PAINEL DE TABELA REUTILIZÁVEL ────────────────────────────────────────────
class PainelTabela(tk.Frame):
    def __init__(self, master, colunas, **kw):
        super().__init__(master, bg=BG, **kw)

        # Tabela
        frame_tree = tk.Frame(self, bg=CARD, bd=0,
                              highlightthickness=1, highlightbackground=BORDER)
        frame_tree.pack(fill="both", expand=True)

        scroll = ttk.Scrollbar(frame_tree, orient="vertical")
        self.tree = ttk.Treeview(frame_tree, columns=colunas, show="headings",
                                 yscrollcommand=scroll.set, selectmode="browse")
        scroll.config(command=self.tree.yview)
        scroll.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        for col in colunas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w", width=120)

        # Zebra
        self.tree.tag_configure("par", background="#1C2128")
        self.tree.tag_configure("impar", background=CARD)

    def limpar(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

    def popular(self, linhas):
        self.limpar()
        for i, linha in enumerate(linhas):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", values=linha, tags=(tag,))

    def selecionado(self):
        sel = self.tree.selection()
        if sel:
            return self.tree.item(sel[0])["values"]
        return None


# ══════════════════════════════════════════════════════════════════════════════
# SECÇÕES
# ══════════════════════════════════════════════════════════════════════════════

class SecaoArtistas(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG)
        self._construir()

    def _construir(self):
        # Cabeçalho
        cab = tk.Frame(self, bg=BG)
        cab.pack(fill="x", padx=24, pady=(20, 10))
        tk.Label(cab, text="🎵  Artistas", bg=BG, fg=FG,
                 font=(FONT, 18, "bold")).pack(side="left")

        # Botões
        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=24, pady=(0, 12))
        BotaoModerno(bf, "+ Adicionar", ACCENT, ACCENT_H, self._adicionar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✎ Atualizar", WARNING, WARNING_H, self._atualizar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✕ Eliminar",  DANGER,  DANGER_H,  self._eliminar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "↺ Atualizar lista", INFO, INFO_H, self._carregar, largura=16).pack(side="right")

        # Tabela
        self.tabela = PainelTabela(self, ["ID", "Nome", "Género"])
        self.tabela.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self._carregar()

    def _carregar(self):
        code, obj = ler_artistas()
        if code == 200:
            self.tabela.popular([(d["id"], d["nome"], d["genero"]) for d in obj.values()])
        else:
            self.tabela.limpar()

    def _adicionar(self):
        d = Dialogo(self, "Adicionar Artista",
                    [("Nome / Banda", "nome"), ("Género Musical", "genero")])
        self.wait_window(d)
        if d.resultado:
            code, obj = criar_artista(d.resultado["nome"], d.resultado["genero"])
            if code == 201:
                messagebox.showinfo("Sucesso", f"Artista {obj['id']} adicionado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _atualizar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um artista primeiro.")
            return
        id_a = str(sel[0]).strip()
        nome_a = str(sel[1]).strip()
        genero_a = str(sel[2]).strip()
        d = Dialogo(self, "Atualizar Artista",
                    [("Nome / Banda", "nome"), ("Género Musical", "genero")],
                    {"nome": nome_a, "genero": genero_a})
        self.wait_window(d)
        if d.resultado:
            import artista as mod_artista
            mod_artista.carregar_artistas()
            if id_a in mod_artista.db_artistas:
                mod_artista.db_artistas[id_a]["nome"]   = d.resultado["nome"] or nome_a
                mod_artista.db_artistas[id_a]["genero"] = d.resultado["genero"] or genero_a
                mod_artista.guardar_artistas()
                messagebox.showinfo("Sucesso", "Artista atualizado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", f"Artista {id_a} não encontrado.")

    def _eliminar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um artista primeiro.")
            return
        id_a = str(sel[0]).strip()
        if messagebox.askyesno("Confirmar", f"Eliminar artista {id_a}?"):
            import artista as mod_artista
            mod_artista.carregar_artistas()
            if id_a in mod_artista.db_artistas:
                del mod_artista.db_artistas[id_a]
                mod_artista.guardar_artistas()
                messagebox.showinfo("Sucesso", f"Artista {id_a} eliminado.")
                self._carregar()
            else:
                messagebox.showerror("Erro", f"Artista {id_a} não encontrado.")


class SecaoBilhetes(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG)
        self._construir()

    def _construir(self):
        cab = tk.Frame(self, bg=BG)
        cab.pack(fill="x", padx=24, pady=(20, 10))
        tk.Label(cab, text="🎟  Bilhetes", bg=BG, fg=FG,
                 font=(FONT, 18, "bold")).pack(side="left")

        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=24, pady=(0, 12))
        BotaoModerno(bf, "+ Emitir",    ACCENT, ACCENT_H, self._emitir).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "🔍 Consultar", INFO,  INFO_H,   self._consultar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✕ Eliminar",  DANGER, DANGER_H, self._eliminar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "↺ Atualizar lista", INFO, INFO_H, self._carregar, largura=16).pack(side="right")

        self.tabela = PainelTabela(self, ["ID", "Concerto", "Tipo", "Lugar", "Fila", "Preço"])
        self.tabela.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self._carregar()

    def _carregar(self):
        code, obj = listar_bilhetes()
        if code == 200:
            self.tabela.popular([
                (b["id"], b["id_concerto"], b["tipo"], b["lugar"], b["fila"], b["preco"])
                for b in obj.values()
            ])
        else:
            self.tabela.limpar()

    def _emitir(self):
        d = Dialogo(self, "Emitir Bilhete", [
            ("ID do Concerto", "id_concerto"),
            ("Preço (€)",      "preco"),
            ("Tipo (VIP/Normal)", "tipo"),
            ("Lugar",          "lugar"),
            ("Fila",           "fila"),
        ])
        self.wait_window(d)
        if d.resultado:
            r = d.resultado
            code, obj = criar_bilhete(r["preco"], r["tipo"], r["lugar"], r["fila"], r["id_concerto"])
            if code == 201:
                messagebox.showinfo("Sucesso", f"Bilhete {obj['id']} emitido!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _consultar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um bilhete primeiro.")
            return
        id_b = sel[0]
        code, obj = consultar_bilhete(str(id_b))
        if code == 200:
            info = "\n".join([f"{k.capitalize()}: {v}" for k, v in obj.items()])
            messagebox.showinfo(f"Bilhete {id_b}", info)
        else:
            messagebox.showerror("Erro", str(obj))

    def _eliminar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um bilhete primeiro.")
            return
        id_b = sel[0]
        if messagebox.askyesno("Confirmar", f"Eliminar bilhete {id_b}?"):
            code, obj = eliminar_bilhete(str(id_b))
            if code == 200:
                messagebox.showinfo("Sucesso", f"Bilhete {id_b} eliminado.")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))


class SecaoStaff(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG)
        self._construir()

    def _construir(self):
        cab = tk.Frame(self, bg=BG)
        cab.pack(fill="x", padx=24, pady=(20, 10))
        tk.Label(cab, text="👥  Staff", bg=BG, fg=FG,
                 font=(FONT, 18, "bold")).pack(side="left")

        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=24, pady=(0, 12))
        BotaoModerno(bf, "+ Registar",  ACCENT,  ACCENT_H,  self._registar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✎ Atualizar", WARNING, WARNING_H, self._atualizar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✕ Remover",   DANGER,  DANGER_H,  self._remover).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "↺ Atualizar lista", INFO, INFO_H, self._carregar, largura=16).pack(side="right")

        self.tabela = PainelTabela(self, ["ID", "Nome", "NIF", "Função", "Telemóvel"])
        self.tabela.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self._carregar()

    def _carregar(self):
        code, obj = listar_staff()
        if code == 200:
            self.tabela.popular([
                (s["id"], s["nome"], s["nif"], s["funcao"], s["telemovel"])
                for s in obj.values()
            ])
        else:
            self.tabela.limpar()

    def _registar(self):
        d = Dialogo(self, "Registar Staff", [
            ("NIF",       "nif"),
            ("Nome",      "nome"),
            ("Função",    "funcao"),
            ("Telemóvel", "telemovel"),
        ])
        self.wait_window(d)
        if d.resultado:
            r = d.resultado
            code, obj = criar_staff(r["nif"], r["nome"], r["funcao"], r["telemovel"])
            if code == 201:
                messagebox.showinfo("Sucesso", f"Funcionário {obj['id']} registado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _atualizar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um membro de staff primeiro.")
            return
        id_s, nome_s, nif_s, funcao_s, tel_s = sel
        d = Dialogo(self, "Atualizar Staff", [
            ("NIF",       "nif"),
            ("Nome",      "nome"),
            ("Função",    "funcao"),
            ("Telemóvel", "telemovel"),
        ], {"nif": nif_s, "nome": nome_s, "funcao": funcao_s, "telemovel": tel_s})
        self.wait_window(d)
        if d.resultado:
            r = d.resultado
            code, obj = atualizar_staff(
                str(id_s),
                r["nif"] or None, r["nome"] or None,
                r["funcao"] or None, r["telemovel"] or None
            )
            if code == 200:
                messagebox.showinfo("Sucesso", "Staff atualizado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _remover(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um membro de staff primeiro.")
            return
        id_s = sel[0]
        if messagebox.askyesno("Confirmar", f"Remover funcionário {id_s}?"):
            code, obj = remover_staff(str(id_s))
            if code == 200:
                messagebox.showinfo("Sucesso", f"Funcionário {id_s} removido.")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))


class SecaoConcertos(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG)
        self._construir()

    def _construir(self):
        cab = tk.Frame(self, bg=BG)
        cab.pack(fill="x", padx=24, pady=(20, 10))
        tk.Label(cab, text="🎤  Concertos", bg=BG, fg=FG,
                 font=(FONT, 18, "bold")).pack(side="left")

        bf = tk.Frame(self, bg=BG)
        bf.pack(fill="x", padx=24, pady=(0, 12))
        BotaoModerno(bf, "+ Marcar",    ACCENT,  ACCENT_H,  self._marcar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✎ Atualizar", WARNING, WARNING_H, self._atualizar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "✕ Cancelar",  DANGER,  DANGER_H,  self._cancelar).pack(side="left", padx=(0, 8))
        BotaoModerno(bf, "↺ Atualizar lista", INFO, INFO_H, self._carregar, largura=16).pack(side="right")

        self.tabela = PainelTabela(self, ["ID", "Nome", "Artista", "Data", "Local"])
        self.tabela.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        self._carregar()

    def _carregar(self):
        code, obj = listar_concertos()
        if code == 200:
            self.tabela.popular([
                (c["id"], c["nome"], c["id_artista"], c["data"], c["local"])
                for c in obj.values()
            ])
        else:
            self.tabela.limpar()

    def _marcar(self):
        d = Dialogo(self, "Marcar Concerto", [
            ("ID do Artista", "id_artista"),
            ("Nome",          "nome"),
            ("Data e Hora",   "data"),
            ("Local",         "local"),
        ])
        self.wait_window(d)
        if d.resultado:
            r = d.resultado
            code, obj = criar_concerto(r["nome"], r["data"], r["local"], r["id_artista"])
            if code == 201:
                messagebox.showinfo("Sucesso", f"Concerto {obj['id']} agendado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _atualizar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um concerto primeiro.")
            return
        id_c, nome_c, _, data_c, local_c = sel
        d = Dialogo(self, "Atualizar Concerto", [
            ("Nome",        "nome"),
            ("Data e Hora", "data"),
            ("Local",       "local"),
        ], {"nome": nome_c, "data": data_c, "local": local_c})
        self.wait_window(d)
        if d.resultado:
            r = d.resultado
            code, obj = atualizar_concerto(
                str(id_c),
                r["nome"] or None, r["data"] or None, r["local"] or None
            )
            if code == 200:
                messagebox.showinfo("Sucesso", "Concerto atualizado!")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))

    def _cancelar(self):
        sel = self.tabela.selecionado()
        if not sel:
            messagebox.showwarning("Aviso", "Seleciona um concerto primeiro.")
            return
        id_c = sel[0]
        if messagebox.askyesno("Confirmar", f"Cancelar concerto {id_c}?"):
            code, obj = eliminar_concerto(str(id_c))
            if code == 200:
                messagebox.showinfo("Sucesso", f"Concerto {id_c} cancelado.")
                self._carregar()
            else:
                messagebox.showerror("Erro", str(obj))


# ══════════════════════════════════════════════════════════════════════════════
# JANELA PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Concertos")
        self.geometry("1000x640")
        self.minsize(900, 560)
        self.configure(bg=BG)
        aplicar_estilos()
        self._construir()

    def _construir(self):
        # ── Sidebar ──────────────────────────────────────────────────────────
        sidebar = tk.Frame(self, bg=SIDEBAR, width=200)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        # Logo
        tk.Label(sidebar, text="🎵", bg=SIDEBAR, fg=ACCENT,
                 font=(FONT, 28)).pack(pady=(28, 4))
        tk.Label(sidebar, text="Gestor de\nConcertos", bg=SIDEBAR, fg=FG,
                 font=(FONT, 12, "bold"), justify="center").pack()
        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=18)

        # Itens de navegação
        self._secoes = {
            "🎵  Artistas":  SecaoArtistas,
            "🎟  Bilhetes":  SecaoBilhetes,
            "👥  Staff":     SecaoStaff,
            "🎤  Concertos": SecaoConcertos,
        }
        self._botoes_nav = {}
        self._frame_ativo = None
        self._secao_cache = {}

        for nome in self._secoes:
            btn = tk.Button(
                sidebar, text=nome, bg=SIDEBAR, fg=FG2,
                font=(FONT, 11), relief="flat", bd=0,
                activebackground=CARD, activeforeground=FG,
                cursor="hand2", anchor="w", padx=20, pady=10,
                command=lambda n=nome: self._navegar(n)
            )
            btn.pack(fill="x")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=CARD, fg=FG) if b != self._btn_ativo else None)
            btn.bind("<Leave>", lambda e, b=btn, n=nome: b.config(
                bg=ACCENT if b == self._btn_ativo else SIDEBAR,
                fg=FG if b == self._btn_ativo else FG2
            ))
            self._botoes_nav[nome] = btn

        self._btn_ativo = None

        # Rodapé sidebar
        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=18, side="bottom")
        tk.Label(sidebar, text="v1.0 · GPSI 1A", bg=SIDEBAR, fg=FG3,
                 font=(FONT, 9)).pack(side="bottom", pady=8)

        # ── Mini player ──────────────────────────────────────────────────────
        tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=(12, 6), side="bottom")

        player_frame = tk.Frame(sidebar, bg=SIDEBAR)
        player_frame.pack(side="bottom", fill="x", padx=14, pady=(0, 4))

        # Playlist
        self._playlist = [
            ("⚡ Thunderstruck",      "AC/DC",            "thunderstruck.mp3"),
            ("🔥 Highway to Hell",    "AC/DC",            "highway_to_hell.mp3"),
            ("💣 TNT",               "AC/DC",            "tnt.mp3"),
            ("🌴 Welcome to the Jungle", "Guns N Roses", "welcome_to_the_jungle.mp3"),
        ]
        self._indice = 0
        self._a_tocar = False

        self._lbl_titulo = tk.Label(player_frame, text=self._playlist[0][0],
                 bg=SIDEBAR, fg=FG2, font=(FONT, 9, "bold"))
        self._lbl_titulo.pack()
        self._lbl_artista = tk.Label(player_frame, text=self._playlist[0][1],
                 bg=SIDEBAR, fg=FG3, font=(FONT, 8))
        self._lbl_artista.pack()

        btn_frame = tk.Frame(player_frame, bg=SIDEBAR)
        btn_frame.pack(pady=6)

        def _atualizar_labels():
            t, a, _ = self._playlist[self._indice]
            self._lbl_titulo.config(text=t)
            self._lbl_artista.config(text=a)

        def _play_pause():
            import os
            _, _, ficheiro = self._playlist[self._indice]
            caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), ficheiro)
            if not os.path.exists(caminho):
                messagebox.showwarning("Música", f"Coloca o ficheiro {ficheiro} na pasta src/.")
                return
            os.startfile(caminho)
            self._a_tocar = True
            btn_play.config(text="⏸")

        def _stop():
            import subprocess
            subprocess.run(["taskkill", "/F", "/IM", "wmplayer.exe"], capture_output=True)
            subprocess.run(["taskkill", "/F", "/IM", "Music.UI.exe"], capture_output=True)
            self._a_tocar = False
            btn_play.config(text="▶")

        def _anterior():
            _stop()
            self._indice = (self._indice - 1) % len(self._playlist)
            _atualizar_labels()

        def _seguinte():
            _stop()
            self._indice = (self._indice + 1) % len(self._playlist)
            _atualizar_labels()

        btn_prev = tk.Button(btn_frame, text="⏮", bg=CARD, fg=FG2,
            activebackground=BORDER, activeforeground=FG,
            font=(FONT, 11), relief="flat", bd=0,
            cursor="hand2", width=3, pady=4, command=_anterior)
        btn_prev.pack(side="left", padx=(0, 4))

        btn_play = tk.Button(btn_frame, text="▶", bg=ACCENT, fg=FG,
            activebackground=ACCENT_H, activeforeground=FG,
            font=(FONT, 12, "bold"), relief="flat", bd=0,
            cursor="hand2", width=3, pady=4, command=_play_pause)
        btn_play.pack(side="left", padx=(0, 4))

        btn_stop = tk.Button(btn_frame, text="⏹", bg=CARD, fg=FG2,
            activebackground=BORDER, activeforeground=FG,
            font=(FONT, 12), relief="flat", bd=0,
            cursor="hand2", width=3, pady=4, command=_stop)
        btn_stop.pack(side="left", padx=(0, 4))

        btn_next = tk.Button(btn_frame, text="⏭", bg=CARD, fg=FG2,
            activebackground=BORDER, activeforeground=FG,
            font=(FONT, 11), relief="flat", bd=0,
            cursor="hand2", width=3, pady=4, command=_seguinte)
        btn_next.pack(side="left")

        # ── Área de conteúdo ─────────────────────────────────────────────────
        self._area = tk.Frame(self, bg=BG)
        self._area.pack(side="left", fill="both", expand=True)

        # Navegar para a primeira secção por defeito
        self._navegar("🎵  Artistas")

    def _navegar(self, nome):
        # Remover frame anterior
        if self._frame_ativo:
            self._frame_ativo.pack_forget()

        # Atualizar botão ativo
        if self._btn_ativo:
            self._btn_ativo.config(bg=SIDEBAR, fg=FG2)
        self._btn_ativo = self._botoes_nav[nome]
        self._btn_ativo.config(bg=ACCENT, fg=FG)

        # Criar secção (ou reutilizar cache)
        if nome not in self._secao_cache:
            self._secao_cache[nome] = self._secoes[nome](self._area)
        self._frame_ativo = self._secao_cache[nome]
        self._frame_ativo.pack(fill="both", expand=True)


# ── ARRANQUE ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    from logger import setup_logging
    setup_logging()
    app = App()
    app.mainloop()
