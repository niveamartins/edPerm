import React from 'react'

import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'

function EditarCadastro() {

    //Integrar cadastro com js

    // mudar quando for integrar:
    // <input placeholder="Nome do Aluno" value={name} onChange={e => setName(e.target.value)}></input>
    // onSubmit={handleCreate}
    // <input placeholder="Código da Turma" value={turma} onChange={e => setTurma(e.target.value)}></input>

    return (
        <div>
            <Accessibility/>
            <NavBar/>

            <main className="main-content-forms">
                <div className="form-page-container">
                    <div className="form-container">
                        <form>
                            <p>Edite suas informações abaixo</p>
                            <input type="text" name="usuario" class="form-input" placeholder="Usuário" required />
                            <input type="text" name="email" class="form-input" placeholder="Email" required></input>
                            <input type="password" name="senha" class="form-input" placeholder="Senha" required />
                            <input type="password" name="confirme_senha" id="confirm_password" class="form-input"
                                placeholder="Confirme a Senha" required />
                            <input type="submit" class="button" value="Editar" />
                    
                        </form>
                    </div>
                </div>
            </main>
            <Footer/>
        </div>
    )
}

export default EditarCadastro