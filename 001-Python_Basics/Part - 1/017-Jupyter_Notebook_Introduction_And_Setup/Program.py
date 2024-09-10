#!/usr/bin/python3
# Jupyter Notebook Introduction And Setup

"""
>>>> Jupyter Notebook
        It is a way to run code interactively in the web browser along with some visualizations and some markdown text to explain the process of what's going on.

        Jupyter project is evolved out of IPython.
>>>> Install Jupyter Notebook using conda and pip.
        Jupyter Notebook comes by default in anaconda.

        Install using pip.
            pip3 install --upgrade pip
            pip3 install notebook

        Open Jupyter Notebook.
            jupyter notebook
>>>> Kernels in Jupyter Notebook
        Kernels are basically what programming language that you want to use.
>>>> Help option in Jupyter Notebook.   
        Refer the "User Interface Tour" and "Keyboard Shortcuts" in the help option.
>>>> Two modes in the Notebook.
        Command mode
            Help to perform actions like adding and deleting cells.
            Get into the command mode by pressing the Esc key. 
            Cell will be in blue color.
        Edit mode
            Help to edit the cell.
            Get into the edit mode by pressing the Enter key.
            Cell will be in green color.
>>>> Executing a cell.
        Execute the cell.
            Ctrl + Enter
        Run cell and select below.
            Shift + Enter
        Run cell and insert below.
            Alt + Enter
>>>> The number on the left side of the cell indicate the execution order.
>>>> Special commands in notebook cell.
        ! (Exclamation mark will interpreted as bash command.)
            !pip list

        Notebook also comes with built-in commands called magic commands.
            These will start with % or %% sign.

            % (The commands arguments will all come from that same line and are called line magics)
                %pwd
                %ls
                %ls -la

                %matplotlib inline
                    It allows matplotlib charts to be displayed within the notebook.

            %% (the entire cell will be used as that's command arguments and are called cell magics)
                # The entire html will be rendered.
                %%HTML
                <div>
                    <h1> Hello World</h1>
                    <p> Thi is a sample <span>paragraph</span> </p>
                </div>


                # Get the execution time for a python code.
                %%timeit
                square_evens = [n*n for n in range(1000)]

            List all the line magics and cell magics command.
                %lsmagic
>>>> We can export the notebook in different formats like html, pdf etc.
>>>> Install python2 kernel in jupyter notebook with pip.
        Reference Link: https://ipython.readthedocs.io/en/latest/install/kernel_install.html
>>>> Gallery of interesting IPython notebooks.
        Reference Link: https://github.com/Carreau/ipython-wiki/blob/master/A-gallery-of-interesting-IPython-Notebooks.md

        You can download various notebook and play around.
"""
