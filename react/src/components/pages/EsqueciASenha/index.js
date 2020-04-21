//página de esqueci a senha
import React from '../../../node_modules/react';

function Inicio() {

    //adaptar login para js
    //fazer mudanças para usar useState
    //mudar links esqueci a senha e cadastro

    return (
        <div className="login-index">
            <div className="index-header">
                <a href="/">Educação Permanente</a>
            </div>

            <main className="main-content-forms">
                <div className="form-page-container">
                    <div className="form-container">
                        <form>
                            <h1>Esqueceu a senha?</h1>
                            <p>Preencha o formulário para receber a senha por e-mail!</p>
                            <input type="text" name = "email" class="form-input" placeholder="E-mail" required />
                            <input type="submit" class="button login" value = "Enviar" />
                        </form>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default Inicio