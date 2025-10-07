import tkinter as tk
from tkinter import ttk, messagebox

class VSSSpecGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("VSS Specification Generator")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Field definitions
        self.fields = [
            ("Full Path", "entry"),
            ("Type", "combobox", ["branch", "sensor", "actuator", "attribute"]),
            ("Datatype", "combobox", ["uint8", "int8", "uint16", "int16", "uint32", "int32", 
                                    "uint64", "int64", "boolean", "float", "double", "string"]),
            ("Description", "entry")
        ]
        
        self.widgets = {}
        row = 0
        
        # Create input fields
        for field in self.fields:
            label = ttk.Label(main_frame, text=f"{field[0]}:")
            label.grid(row=row, column=0, sticky=tk.W, pady=2)
            
            if field[1] == "entry":
                widget = ttk.Entry(main_frame, width=50)
            else:
                widget = ttk.Combobox(main_frame, values=field[2], width=47, state="readonly")
            
            widget.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
            self.widgets[field[0]] = widget
            row += 1
        
        # Add trace to Type combobox to handle branch case
        self.widgets["Type"].bind('<<ComboboxSelected>>', self.on_type_change)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Add Entry", command=self.add_entry).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save File", command=self.save_file).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        
        # Text area for preview
        ttk.Label(main_frame, text="Preview:").grid(row=row+1, column=0, sticky=tk.W, pady=(10,0))
        self.preview_text = tk.Text(main_frame, width=60, height=15, wrap=tk.NONE)
        self.preview_text.grid(row=row+2, column=0, columnspan=2, pady=5)
        
        # Scrollbars for text area
        v_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.preview_text.yview)
        v_scrollbar.grid(row=row+2, column=2, sticky=(tk.N, tk.S))
        self.preview_text.configure(yscrollcommand=v_scrollbar.set)
        
        h_scrollbar = ttk.Scrollbar(main_frame, orient=tk.HORIZONTAL, command=self.preview_text.xview)
        h_scrollbar.grid(row=row+3, column=0, columnspan=2, sticky=(tk.W, tk.E))
        self.preview_text.configure(xscrollcommand=h_scrollbar.set)
        
        # Initialize
        self.spec_content = []
        self.clear_all()
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(row+2, weight=1)

    def on_type_change(self, event):
        """Handle type selection change - disable datatype for branches"""
        selected_type = self.widgets["Type"].get()
        if selected_type == "branch":
            self.widgets["Datatype"].set('')  # Clear datatype
            self.widgets["Datatype"].config(state="disabled")
        else:
            self.widgets["Datatype"].config(state="readonly")

    def add_entry(self):
        """Add current field values to the specification"""
        path = self.widgets["Full Path"].get().strip()
        type_val = self.widgets["Type"].get()
        datatype_val = self.widgets["Datatype"].get()
        description = self.widgets["Description"].get().strip()
        
        # Validation
        if not path:
            messagebox.showerror("Error", "Full Path is required!")
            return
        
        if not type_val:
            messagebox.showerror("Error", "Type is required!")
            return
        
        # For non-branch types, datatype is required
        if type_val != "branch" and not datatype_val:
            messagebox.showerror("Error", f"Datatype is required for {type_val}!")
            return
        
        # Add to specification
        entry_lines = [f"{path}:"]
        entry_lines.append(f"  type: {type_val}")
        
        # Only include datatype for non-branch types
        if type_val != "branch" and datatype_val:
            entry_lines.append(f"  datatype: {datatype_val}")
        
        if description:
            entry_lines.append(f"  description: {description}")
        
        entry_lines.append("")  # Empty line for separation
        
        # Add to content and update preview
        self.spec_content.extend(entry_lines)
        self.update_preview()
        
        # Clear fields for next entry (but maintain type selection)
        current_type = self.widgets["Type"].get()
        self.clear_fields()
        self.widgets["Type"].set(current_type)
        self.on_type_change(None)  # Update datatype field state

    def clear_fields(self):
        """Clear input fields but keep previous values in dropdowns"""
        self.widgets["Full Path"].delete(0, tk.END)
        self.widgets["Description"].delete(0, tk.END)
        # Don't clear the type selection, but reset datatype based on type
        if self.widgets["Type"].get() == "branch":
            self.widgets["Datatype"].set('')
        # Leave datatype as is for other types to maintain common choices

    def clear_all(self):
        """Clear all inputs and the specification"""
        self.spec_content = []
        for field_name, widget in self.widgets.items():
            if isinstance(widget, ttk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.set('')
        # Enable datatype field initially
        self.widgets["Datatype"].config(state="readonly")
        self.update_preview()

    def update_preview(self):
        """Update the preview text area"""
        self.preview_text.delete(1.0, tk.END)
        self.preview_text.insert(1.0, "".join(line + "\n" for line in self.spec_content))

    def save_file(self):
        """Save the specification to custom_vss.spec"""
        if not self.spec_content:
            messagebox.showwarning("Warning", "No specification content to save!")
            return
        
        try:
            with open("custom_vss.vspec", "w", encoding="utf-8") as f:
                f.write("".join(line + "\n" for line in self.spec_content))
            messagebox.showinfo("Success", "Specification saved to custom_vss.spec")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VSSSpecGenerator(root)
    root.mainloop()