Figures
=======

.. prf:theorem:: A numbered theorem
   :label: thm-numbered

   .. figure:: plot.png
      :name: fig-numbered-theorem

      Figure in a numbered theorem

.. prf:lemma:: An unnumbered lemma
   :label: lem-nonumber
   :nonumber:

   .. figure:: plot.png
      :name: fig-unnumbered-lemma

      Figure in an unnumbered lemma

.. prf:proof::

   A proof with a figure.

   .. figure:: plot.png
      :name: fig-proof

      Figure in a proof

.. note::

   .. figure:: plot.png
      :name: fig-note

      Figure in a note

.. prf:theorem:: A theorem with a nested lemma
   :label: thm-nested

   .. prf:lemma:: A lemma inside a theorem
      :label: lem-nested
      :nonumber:

      .. figure:: plot.png
         :name: fig-nested-lemma

         Figure in a lemma inside a theorem

   .. figure:: plot.png
      :name: fig-after-nested-lemma

      Figure in a theorem after its nested lemma

.. note::

   .. prf:definition:: A definition inside a note
      :label: def-in-note

      .. figure:: plot.png
         :name: fig-definition-in-note

         Figure in a definition inside a note

.. figure:: plot.png
   :name: fig-outside

   Figure outside any box
